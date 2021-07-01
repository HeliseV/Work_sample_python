"""A video player class."""
import random

from .video_library import VideoLibrary


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.is_playing = False
        self.is_paused = False
        self.currently_playing = "None"

    def Video_Name(self, video_id):
        video = self._video_library.get_video(video_id)
        return video.title
    def Video_Tag(self, tags):
        video = self._video_library.get_video(tags)
        return video.tags

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        video = self._video_library.get_all_videos()
        for vid in video:
            print(f"{vid.title} ({vid.video_id}) [{' '.join(vid.tags)}]")


    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        video = self._video_library.get_video(video_id)
        try:
            temp = video.title
            if self.is_playing == False:
                print(f"Playing video: {video.title}")
                self.is_playing = True
                self.is_paused = False
                self.currently_playing = video_id
            else:
                print(f"Stopping video: {self.Video_Name(self.currently_playing)}")
                print(f"Playing video: {video.title}")
                self.currently_playing = video_id
                self.is_paused = False
        except:
            print("Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video."""
        try:
            if self.is_playing == True or self.is_paused == True:
                print(f"Stopping video: {self.Video_Name(self.currently_playing)}")
                self.is_playing = False
                self.is_paused = False
            else:
                print("Cannot stop video: No video is currently playing")
        except:
            print("Cannot stop video: No video is currently playing")



    def play_random_video(self):
        """Plays a random video from the video library."""
        number_of_videos = len(self._video_library.get_all_videos())-1
        random_video = random.randint(0, number_of_videos)
        video = self._video_library.get_all_videos()
        try:
            video_id = video[random_video].video_id
            if self.is_playing == False:
                print(f"Playing video: {video[random_video].title}")
                self.is_playing = True
                self.is_paused = False
                self.currently_playing = video_id
            else:
                print(f"Stopping video: {self.Video_Name(self.currently_playing)}")
                print(f"Playing video: {video[random_video].title}")
                self.currently_playing = video_id
                self.is_paused = False
        except:
            print("Cannot play video: Video does not exist")

    def pause_video(self):
        """Pauses the current video."""
        try:
            if self.is_paused == False:
                print(f"Pausing video: {self.Video_Name(self.currently_playing)}")
                self.is_playing = False
                self.is_paused = True
            elif self.is_paused == True:
                print(f"Video already paused: {self.Video_Name(self.currently_playing)}")
            else:
                print("Cannot pause video: No video is currently playing")
        except:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""
        try:
            if self.is_paused == True:
                print(f"Continuing video: {self.Video_Name(self.currently_playing)}")
                self.is_playing = True
                self.is_paused = False
            elif self.is_playing == True:
                print("Cannot continue video: Video is not paused")
            else:
                print("Cannot continue video: No video is currently playing")
        except:
            print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""
        try:
            if self.is_paused == True:
                print(f"{self.Video_Name(self.currently_playing)} ({self.currently_playing}) [{' '.join(self.Video_Tag(self.currently_playing))}] - PAUSED")
            elif self.is_playing == True:
                print(f"{self.Video_Name(self.currently_playing)} ({self.currently_playing}) [{' '.join(self.Video_Tag(self.currently_playing))}]")
            else:
                print("No video is currently playing")
        except:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
