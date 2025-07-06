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
    for row in cursor.fetchall():
        print(row)

def add_video():
    name = input("Enter the video name: ")
    time = input("Enter the video time: ")
    cursor.execute("INSERT INTO videos (name,time) VALUES (?,?)",(name,time))
    conn.commit()
    
def update_video():
    video_id = input("Enter the video ID to update: ")
    new_name = input("Enter the name: ")
    new_time = input("Enter the video time: ")
    
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?",(new_name,new_time,video_id))
    
    conn.commit()
def delete_video():
    video_id = input("Enter the Video ID to delete: ")
    cursor.execute("DELETE FROM videos WHERE id = ?",(video_id,)) #here the trailing comma is important
    conn.commit()

def main():
    while True:
        videos = []
        print("\n Youtube Manager App with DB")
        print("1. List all Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit App")
        choice = input("Enter your choice:  ")
        
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