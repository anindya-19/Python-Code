import sqlite3

conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()
cursor.execute('''
               CREATE TABLE IF NOT EXISTS videos(
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    time TEXT NOT NULL
               )
               ''')

def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    rows = cursor.fetchall()
    if not rows:
        print("No videos found!")
        return
    else:
        for row in rows:
            print(row)

def add_video():
    name = input("Enter the video name: ")
    time = input("Enter the video time: ")
    if not name or not time:
        print("Name and Time cannot be empty!")
        return
    cursor.execute("INSERT INTO videos (name,time) VALUES (?,?)",(name,time))
    conn.commit()
    print("The video was added successfully!")
    
def update_video():
    video_id = input("Enter the video ID to update: ").strip()
    new_name = input("Enter the name: ")
    new_time = input("Enter the video time: ")
    if not new_name or not new_time:
        print("Name and time cannot be empty!!")
        return
    rec = cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?",(new_name,new_time,video_id))
    if rec.rowcount == 0:
        print("No video found with that ID")
        return
    else:
        print("The data was updated successfully!")
        conn.commit()

def delete_video():
    video_id = input("Enter the Video ID to delete: ")
    if not video_id.isdigit():
        print("Please enter a valid ID!")
        return
    rec = cursor.execute("DELETE FROM videos WHERE id = ?",(video_id,)) #here the trailing comma is important
    if rec.rowcount == 0:
        print("No Video found with that ID!")
        return
    else:
        print("Data deleted successfully!")
        conn.commit()

def main():
    while True:
        print("\n *________Youtube Manager App with DB || Please enter your option_________*")
        print("1. List all Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit App")
        choice = input("Enter your choice:  ").strip()
        
        match choice:
            case '1':
                list_all_videos()
            case '2':
                add_video()
            case '3':
                update_video()
            case '4':
                delete_video()
            case '5':
                print("Thanks for using the YouTube manager app!!")
                break
            case  _:
                print("Invalid Choice!")

    conn.close()
if __name__ == '__main__':
    main()