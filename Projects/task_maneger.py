import pandas as pd
import smtplib
from email.message import EmailMessage

# Initialize an empty DataFrame for tasks
columns = ["task", "name", "due date", "sent"]
task_df = pd.DataFrame(columns=columns)

# Hashmap to map names to emails
mail_hashmap = {
    "yonatan landesman": "yonatanlan7@gmail.com",
    "john doe": "yonatanlan7@gmail.com",
    "jane smith": "yonatanlan7@gmail.com"
}

def request_user_email(name):
    """Placeholder function to request and add a new email to the hashmap."""
    print(f"Name '{name}' not found in the email hashmap.")
    email = input(f"Enter email for {name}: ")
    mail_hashmap[name] = email
    print(f"Added {name} to hashmap.")

def add_tasks_batch(data_string):
    """Adds multiple tasks to the DataFrame from a formatted string."""
    global task_df
    entries = data_string.split("/")
    new_tasks = []
  
    for entry in entries:
        task, name, due_date = entry.split(", ")
        name = name.lower()
        if name not in mail_hashmap:
            request_user_email(name)
        new_tasks.append([task, name, due_date, "Not Sent"])
    
    if new_tasks:
        new_task_df = pd.DataFrame(new_tasks, columns=columns)
        task_df = pd.concat([task_df, new_task_df], ignore_index=True)
        print("Tasks added successfully!")

def save_to_excel(filename="tasks.xlsx"):
    """Saves the DataFrame to an Excel file."""
    task_df.to_excel(filename, index=False)
    print(f"Tasks saved successfully to {filename}!")

def load_from_excel(filename="tasks.xlsx"):
    """Loads tasks from an Excel file into the DataFrame."""
    global task_df
    try:
        task_df = pd.read_excel(filename)
        print(f"Tasks loaded successfully from {filename}!")
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with an empty task list.")

def map_tasks_to_emails():
    """Maps all 'Not Sent' tasks to corresponding emails."""
    email_tasks = {}
    not_sent_tasks = task_df[task_df["sent"] == "Not Sent"]
    
    for _, row in not_sent_tasks.iterrows():
        name = row["name"].lower()
        task_info = f"{row['task']} (Due: {row['due date']})"
        
        if name not in mail_hashmap:
            request_user_email(name)
        
        email = mail_hashmap[name]
        if email not in email_tasks:
            email_tasks[email] = []
        email_tasks[email].append(task_info)
    
    return email_tasks

def send_tasks_via_smtp(email_tasks, sender_email, sender_password):
    """Sends emails with tasks using Outlook's SMTP server and updates status if sent successfully."""
    smtp_server = "smtp.office365.com"
    smtp_port = 587
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        
        for recipient_email, tasks in email_tasks.items():
            msg = EmailMessage()
            msg["From"] = sender_email
            msg["To"] = recipient_email
            msg["Subject"] = "Your Pending Tasks"
            
            task_list = "\n".join([f"- {task}" for task in tasks])
            msg.set_content(f"Hello,\n\nHere are your pending tasks:\n\n{task_list}\n\nPlease make sure to complete them on time.\n\nBest regards,\nTask Manager")
            
            server.send_message(msg)
            print(f"Email sent to {recipient_email}")
            
            # Update the sent status in the DataFrame
            for i in task_df.index:
                if task_df.at[i, "name"].lower() in mail_hashmap and mail_hashmap[task_df.at[i, "name"].lower()] == recipient_email:
                    task_df.at[i, "sent"] = "Sent"
        
        server.quit()
        print("All emails sent successfully!")
    except Exception as e:
        print(f"Error sending emails: {e}")

def display_tasks():
    """Displays the current tasks."""
    if task_df.empty:
        print("No tasks available.")
    else:
        print(task_df)

# Example usage:
load_from_excel()
data_input = input("Enter tasks (format: task, name, due date/task, name, due date/...): ")
add_tasks_batch(data_input)
display_tasks()
mapped_tasks = map_tasks_to_emails()
print("\nMapped Tasks to Emails:")
print(mapped_tasks)
sender_email = 'yonatanlan7@gmail.com' # input("Enter your Outlook email: ")
sender_password = 'nyumjrotenhpfxcl' # input("Enter your Outlook password: ")
send_tasks_via_smtp(mapped_tasks, sender_email, sender_password)
save_to_excel()