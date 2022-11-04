import sys

from Y2F_PACKAGE import Graphical_User_Interface, Youtube_Content_Operations


def Youtube_Download():
    gui = Graphical_User_Interface.Graphical_User_Interfaces_For_Menus_And_Messages("link request menu")
    youtube_link = gui.Graphical_User_Interface_Selector()

    if youtube_link == "_BACK":
        main_entry_point()

    gui = Graphical_User_Interface.Graphical_User_Interfaces_For_Menus_And_Messages("path selection menu")
    selected_path = gui.Graphical_User_Interface_Selector()

    if selected_path == "_BACK":
        main_entry_point()

    selected_resolution = Video_Resolution_Selection()

    gui = Graphical_User_Interface.Graphical_User_Interfaces_For_Menus_And_Messages("video downloading warning")
    gui.Graphical_User_Interface_Selector()

    file_download = Youtube_Content_Operations.Operations("youtube video download", youtube_link, selected_path, selected_resolution)
    file_download_result = file_download.Operation_Selection()


    message = file_download_result
    Message_Displayer(message)


def Youtube_Conversion():
    gui = Graphical_User_Interface.Graphical_User_Interfaces_For_Menus_And_Messages("link request menu")
    youtube_link = gui.Graphical_User_Interface_Selector()

    if youtube_link == "_BACK":
        main_entry_point()

    gui = Graphical_User_Interface.Graphical_User_Interfaces_For_Menus_And_Messages("path selection menu")
    selected_path = gui.Graphical_User_Interface_Selector()

    if selected_path == "_BACK":
        main_entry_point()

    gui = Graphical_User_Interface.Graphical_User_Interfaces_For_Menus_And_Messages("video downloading warning")
    gui.Graphical_User_Interface_Selector()

    file_download = Youtube_Content_Operations.Operations("youtube video conversion", youtube_link, selected_path, None)
    file_download_result = file_download.Operation_Selection()

    message = file_download_result
    Message_Displayer(message)


def Video_Resolution_Selection():
    gui = Graphical_User_Interface.Graphical_User_Interfaces_For_Menus_And_Messages("resolution selection menu")
    selected_resolution = gui.Graphical_User_Interface_Selector()

    if selected_resolution == "144p":
        return selected_resolution
    elif selected_resolution == "240p":
        return selected_resolution
    elif selected_resolution == "360p":
        return selected_resolution
    elif selected_resolution == "480p":
        return selected_resolution
    elif selected_resolution == "720p":
        return selected_resolution
    elif selected_resolution == "1080p":
        return selected_resolution
    elif selected_resolution == "1440p":
        return selected_resolution
    elif selected_resolution == "2160p":
        return selected_resolution
    elif selected_resolution == "_BACK":
        return selected_resolution
    else:
        Video_Resolution_Selection()


def Message_Displayer(gui_message):

    try:
        selected_gui = None

        if gui_message is not None:
            if gui_message == "pytube missing":
                selected_gui = "module not found"
            elif gui_message == "wrong path":
                selected_gui = "path not found"
            elif gui_message == "internal error":
                selected_gui = "unknown error"
            elif gui_message == "wrong link":
                selected_gui = "wrong link"
            else:
                selected_gui = "download successful"

        gui = Graphical_User_Interface.Graphical_User_Interfaces_For_Menus_And_Messages(selected_gui)
        gui.Graphical_User_Interface_Selector()

        gui = Graphical_User_Interface.Graphical_User_Interfaces_For_Menus_And_Messages("clear screen")
        gui.Graphical_User_Interface_Selector()

        main_entry_point()
    except KeyboardInterrupt:
        sys.exit(0)


def main_entry_point():
    gui = Graphical_User_Interface.Graphical_User_Interfaces_For_Menus_And_Messages("main menu")
    selected_input = gui.Graphical_User_Interface_Selector()

    if selected_input == "D":
        Youtube_Download()
    elif selected_input == "C":
        Youtube_Conversion()
    elif selected_input == "E":
        gui = Graphical_User_Interface.Graphical_User_Interfaces_For_Menus_And_Messages("clear screen")
        gui.Graphical_User_Interface_Selector()
        sys.exit(0)
    else:
        main_entry_point()


if __name__ == "__main__":
    main_entry_point()
