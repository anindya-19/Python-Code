import json
FILE_NAME = 'youtube.txt'
def load_data():
    try:
        with open(FILE_NAME,'r') as fp:
            return json.load(fp)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open(FILE_NAME,'w') as fp:
        json.dump(videos,fp)

def list_all_videos(videos):
    print("\n")
    print("*" * 50)
    for index,video in enumerate(videos,start=1):
        print(f"{index} {video['name']}, Duration: {video['time']}")
    print("\n")
    print("*" * 50)
        
def add_video(videos):
    name = input("Enter the name of the video: ")
    time = input("Enter video time: ")
    videos.append({'name':name,'time':time})
    save_data_helper(videos)
    
def update_video(video):
    list_all_videos(video)
    index = int(input("Enter the video number to update: "))
    if 1 <= index <= len(video):
        newName = input("Enter the new video name: ")
        newTime = input("Enter the new video time: ")
        video[index-1] = {'name':newName, 'time':newTime}
        save_data_helper(video)
    else:
        print("Invalid Index Selected!!")
        
def delete_video(video):
    list_all_videos(video)
    index = int(input("Enter the video number to be deleted: "))
    
    if 1 <= index <= len(video):
        del video[index-1]
        save_data_helper(video)
        print("Video has been deleted Successfully!")
    else:
        print("Invalid Index of Video!!")

def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager Options")
        print("1. List all youtube videos")
        print("2. Add a YouTube video")
        print("3. Update a  youtube video details")
        print("4. Delete a  youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")
        #print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case  _:
                print("Invalid Choice!")

if __name__ == "__main__":
    main()
