# Importing Required Modules & libraries
from tkinter import *
import pygame
import os


# Defining MusicPlayer Class
class CITCoolMP3:
    """CIT Cool MP3 is a simple music app with only a capability of playing music for now! """
    # Defining Constructor
    def __init__(self, root):
        self.root = root
        # Title of the window
        self.root.title("CIT Cool MP3")
        # Window Geometry
        self.root.geometry("1000x200+200+200")
        # Initiating Pygame
        pygame.init()
        # Initiating Pygame Mixer
        pygame.mixer.init()
        # Declaring track Variable
        self.track = StringVar()
        # Declaring Status Variable
        self.status = StringVar()

        # Creating Track Frame for Song label & status label
        track_frame = LabelFrame(self.root, text="Song Track", font=("times new roman", 15, "bold"), bg="grey",
                                fg="white", bd=5, relief=GROOVE)
        track_frame.place(x=0, y=0, width=600, height=100)
        # Inserting Song Track Label
        song_track = Label(track_frame, textvariable=self.track, width=20, font=("times new roman", 24, "bold"),
                          bg="grey", fg="gold").grid(row=0, column=0, padx=10, pady=5)
        # Inserting Status Label
        track_status = Label(track_frame, textvariable=self.status, font=("times new roman", 24, "bold"), bg="grey",
                            fg="gold").grid(row=0, column=1, padx=10, pady=5)

        # Creating Button Frame
        button_frame = LabelFrame(self.root, text="Control Panel", font=("times new roman", 15, "bold"), bg="grey",
                                 fg="white", bd=5, relief=GROOVE)
        button_frame.place(x=0, y=100, width=600, height=100)

        # Play Button
        play_btn = Button(button_frame, text="PLAY", command=self.play_song, width=6, height=1,
                         font=("times new roman", 16, "bold"), fg="navyblue", bg="gold").grid(row=0, column=0, padx=10,
                                                                                              pady=5)
        # Pause Button
        pause_btn = Button(button_frame, text="PAUSE", command=self.pause_song, width=8, height=1,
                         font=("times new roman", 16, "bold"), fg="navyblue", bg="gold").grid(row=0, column=1, padx=10,
                                                                                              pady=5)
        # Resume Button -- Currently this button is not working and showing
        """Need to change the geometry and button display + functionality"""
        resume_btn = Button(button_frame, text="RESUME", command=self.resume_song, width=10, height=1,
                         font=("times new roman", 16, "bold"), fg="navyblue", bg="gold").grid(row=0, column=2, padx=10,
                                                                                              pady=5)
        # Stop Button
        stop_btn = Button(button_frame, text="STOP", command=self.stop_song, width=6, height=1,
                         font=("times new roman", 16, "bold"), fg="navyblue", bg="gold").grid(row=0, column=3, padx=10,
                                                                                              pady=5)
        # Rewind button
        rewind_btn = Button(button_frame, text="REWIND", command=self.rewind_song, width=10, height=1,
                             font=("times new roman", 16, "bold"), fg="navyblue", bg="gold").grid(row=0, column=2,
                                                                                                  padx=10,
                                                                                                  pady=5)

        # Creating Playlist Frame
        songs_frames = LabelFrame(self.root, text="Song Playlist", font=("times new roman", 15, "bold"), bg="grey",
                                fg="white", bd=5, relief=GROOVE)
        songs_frames.place(x=600, y=0, width=400, height=200)

        # Inserting scrollbar
        scroll_bar = Scrollbar(songs_frames, orient=VERTICAL)

        # Inserting Playlist listbox
        self.playlist = Listbox(songs_frames, yscrollcommand=scroll_bar.set, selectbackground="gold", selectmode=SINGLE,
                                font=("times new roman", 12, "bold"), bg="silver", fg="navyblue", bd=5, relief=GROOVE)

        # Applying Scrollbar to listbox
        scroll_bar.pack(side=RIGHT, fill=Y)
        scroll_bar.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)

        # Directory for fetching Songs
        # TODO: Change this to base directory and be used in all systems
        # for dev mode, we need a button for loading music unto the tray
        os.chdir(r"C:\Users\Ronnie Atuhaire\Desktop\Ronlin\Xiki\MP3")

        # Fetching Songs
        song_tracks = os.listdir()
        # Inserting Songs into Playlist
        for track in song_tracks:
            self.playlist.insert(END, track)

    # Defining Play Song Function
    def play_song(self):
        # Displaying Selected Song title
        self.track.set(self.playlist.get(ACTIVE))
        # Displaying Status
        self.status.set("--Playing--")
        # Loading Selected Song
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        # Playing Selected Song
        pygame.mixer.music.play()

    # Defining Button Functions
    def stop_song(self):
        # Displaying Status
        self.status.set("--Stopped--")
        pygame.mixer.music.stop()

    def pause_song(self):
        # Displaying Status
        self.status.set("--Paused--")
        pygame.mixer.music.pause()

    def resume_song(self):
        # Displaying Status
        self.status.set("--Playing--")
        pygame.mixer.music.unpause()

    def rewind_song(self):
        # Rewind
        self.status.set('--Rewind--')
        pygame.mixer.music.rewind()

    # WORKS IN PROGRESS -->
    def next_song(self):
        pass

    def prev_song(self):
        pass

    def load_music(self):
        pass


# Creating TK Container
root = Tk()
# Creating our own icon
root.iconbitmap(r"images_icons\cit_2.ico")
# Passing Root to MusicPlayer Class
CITCoolMP3(root)
# Root Window Looping
root.mainloop()
