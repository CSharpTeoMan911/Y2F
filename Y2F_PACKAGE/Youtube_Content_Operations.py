import os
import sys

import ffmpeg


class Operations:
    audio_only = False
    chosen_operation = None
    chosen_path = None
    youtube_link = None
    selected_video_resolution = None

    def __init__(self, init_chosen_operation, init_youtube_link, init_chosen_path, init_selected_video_resolution):
        self.chosen_operation = init_chosen_operation
        self.chosen_path = init_chosen_path
        self.youtube_link = init_youtube_link
        self.selected_video_resolution = init_selected_video_resolution

    def Operation_Selection(self):
        if self.chosen_operation == "youtube video conversion":
            self.audio_only = True
        else:
            self.audio_only = False

        download_result = self.__Youtube_Download()
        return download_result

    def __Youtube_Download(self):
        try:
            import pytube.exceptions
            try:
                try:
                    try:
                        try:
                            try:
                                try:
                                    try:
                                        try:
                                            try:
                                                try:
                                                    try:
                                                        try:
                                                            try:
                                                                try:
                                                                    try:
                                                                        from pytube import YouTube

                                                                        youtube_object = YouTube(self.youtube_link)

                                                                        if self.selected_video_resolution is None:
                                                                            video_audio = youtube_object.streams.filter(
                                                                                only_audio=self.audio_only).first()

                                                                            audio_path = video_audio.download(
                                                                                max_retries=3,
                                                                                output_path=self.chosen_path)
                                                                            return audio_path

                                                                        else:
                                                                            from ffmpeg import input
                                                                            from ffmpeg import output

                                                                            if self.selected_video_resolution == "1080p":
                                                                                try:
                                                                                    video_audio = youtube_object.streams.filter(
                                                                                        only_audio=True).first()

                                                                                    audio_path = video_audio.download(
                                                                                        max_retries=3,
                                                                                        output_path=self.chosen_path,
                                                                                        filename="audio.mp3")

                                                                                    video_audio = youtube_object.streams.filter(
                                                                                        only_video=True,
                                                                                        res=self.selected_video_resolution).first()

                                                                                    video_path = video_audio.download(
                                                                                        max_retries=3,
                                                                                        output_path=self.chosen_path)

                                                                                    audio = ffmpeg.input(audio_path)

                                                                                    video = ffmpeg.input(video_path)

                                                                                    path = ffmpeg.output(audio,
                                                                                                         video,
                                                                                                         video_path + "video.mp4")

                                                                                    ffmpeg.run(path,
                                                                                               overwrite_output=True)

                                                                                    os.remove(audio_path)
                                                                                    os.remove(video_path)

                                                                                    return video_path

                                                                                except ffmpeg.Error:
                                                                                    return "wrong path"
                                                                            elif self.selected_video_resolution == "1440p":
                                                                                try:
                                                                                    video_audio = youtube_object.streams.filter(
                                                                                        only_audio=True).first()

                                                                                    audio_path = video_audio.download(
                                                                                        max_retries=3,
                                                                                        output_path=self.chosen_path,
                                                                                        filename="audio.mp3")

                                                                                    video_audio = youtube_object.streams.filter(
                                                                                        only_video=True,
                                                                                        res=self.selected_video_resolution).first()

                                                                                    video_path = video_audio.download(
                                                                                        max_retries=3,
                                                                                        output_path=self.chosen_path)

                                                                                    audio = ffmpeg.input(audio_path)

                                                                                    video = ffmpeg.input(video_path)

                                                                                    path = ffmpeg.output(audio,
                                                                                                         video,
                                                                                                         video_path + "video.mp4")

                                                                                    ffmpeg.run(path,
                                                                                               overwrite_output=True)

                                                                                    os.remove(audio_path)
                                                                                    os.remove(video_path)

                                                                                    return video_path

                                                                                except ffmpeg.Error:
                                                                                    return "wrong path"
                                                                            elif self.selected_video_resolution == "2160p":
                                                                                try:
                                                                                    video_audio = youtube_object.streams.filter(
                                                                                        only_audio=True).first()

                                                                                    audio_path = video_audio.download(
                                                                                        max_retries=3,
                                                                                        output_path=self.chosen_path,
                                                                                        filename="audio.mp3")

                                                                                    video_audio = youtube_object.streams.filter(
                                                                                        only_video=True,
                                                                                        res=self.selected_video_resolution).first()

                                                                                    video_path = video_audio.download(
                                                                                        max_retries=3,
                                                                                        output_path=self.chosen_path)

                                                                                    audio = ffmpeg.input(audio_path)

                                                                                    video = ffmpeg.input(video_path)

                                                                                    path = ffmpeg.output(audio,
                                                                                                         video,
                                                                                                         video_path + "video.mp4")

                                                                                    ffmpeg.run(path,
                                                                                               overwrite_output=True)

                                                                                    os.remove(audio_path)
                                                                                    os.remove(video_path)

                                                                                    return video_path

                                                                                except ffmpeg.Error:
                                                                                    return "wrong path"
                                                                            else:
                                                                                video_audio = youtube_object.streams.filter(
                                                                                    only_audio=self.audio_only,
                                                                                    res=self.selected_video_resolution).first()

                                                                                path = video_audio.download(
                                                                                    output_path=self.chosen_path,
                                                                                    max_retries=3)

                                                                                return path


                                                                    except pytube.exceptions.RecordingUnavailable:
                                                                        return "internal error"
                                                                except pytube.exceptions.Pattern:
                                                                    return "internal error"
                                                            except pytube.exceptions.MembersOnly:
                                                                return "internal error"
                                                        except pytube.exceptions.MaxRetriesExceeded:
                                                            return "internal error"
                                                    except pytube.exceptions.LiveStreamError:
                                                        return "internal error"
                                                except pytube.exceptions.HTMLParseError:
                                                    return "internal error"
                                            except pytube.exceptions.AgeRestrictedError:
                                                return "internal error"
                                        except pytube.exceptions.VideoPrivate:
                                            return "internal error"
                                    except pytube.exceptions.ExtractError:
                                        return "internal error"
                                except pytube.exceptions.PytubeError:
                                    return "internal error"
                            except TypeError:
                                return "internal error"
                        except ValueError:
                            return "internal error"
                    except FileNotFoundError:
                        return "wrong path"
                except KeyboardInterrupt:
                    sys.exit(0)
            except pytube.exceptions.RegexMatchError:
                return "wrong link"
        except ModuleNotFoundError:
            return "pytube missing"
