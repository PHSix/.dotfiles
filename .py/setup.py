import os


def shell_call(cmd: str):
    print("execing cmd: {cmd}".format(cmd=cmd))
    try:
        os.system(cmd)
    except:
        print("exec failed")


if __name__ == "__main__":
    dotfile_env = os.environ.get("DOTFILES_PATH")

    if dotfile_env == "" or dotfile_env == None:
        print("please expect your `DOTFILES_PATH` environment variable.")
        exit(1)

    path = os.path.abspath(dotfile_env)

    # prepare
    shell_call("mkdir ~/.config")

    link_folders = [
        ".config/wezterm",
        ".config/kitty",
        ".config/alacritty",
        ".config/emacs",
        ".config/yazi",
        ".vim",
        ".zshrc",
        ".tmux.conf",
        ".ideavimrc",
    ]

    for f in link_folders:
        shell_call(
            "ln -s {dotfiles_path}/{folder} ~/{folder}".format(
                dotfiles_path=path, folder=f
            )
        )

    print("setup finish")
