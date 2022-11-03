import sys


class Operations:
    audio_only = False
    chosen_operation = None
    chosen_path = None
    youtube_link = None

    def __init__(self, init_chosen_operation, init_youtube_link, init_chosen_path):
        self.chosen_operation = init_chosen_operation
        self.chosen_path = init_chosen_path
        self.youtube_link = init_youtube_link

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
                                                                    from pytube import YouTube

                                                                    youtube_object = YouTube(self.youtube_link)

                                                                    video_audio = youtube_object.streams.filter(
                                                                        only_audio=self.audio_only).first()

                                                                    path = video_audio.download(
                                                                        output_path=self.chosen_path, max_retries=3)
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



