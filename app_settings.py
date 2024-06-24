from pathlib import Path
import yaml


class AppSettings:
    def __init__(
        self,
        wg_path: str ="/usr/bin/wg",
        wg_quick_path: str ="/usr/bin/wg-quick",
        wg_dir: str ="/etc/wireguard",
        peer_config_dir: str ="/etc/wireguard",
    ):
        self.wg_path = wg_path
        self.wg_quick_path = wg_quick_path
        self.wg_dir = wg_dir
        self.peer_config_dir = peer_config_dir

    @classmethod
    def from_file(cls, file_path: str) -> "AppSettings":
        settings_obj = AppSettings()
        if not Path(file_path).exists():
            raise ValueError(f"File {file_path} does not exist")
        
        with open(file_path, "r") as f:
            settings_dict = yaml.load(f, Loader=yaml.FullLoader)
            settings_obj.wg_path = settings_dict.get("wg_path", "/usr/bin/wg")
            settings_obj.wg_quick_path = settings_dict.get(
                "wg_quick_path", "/usr/bin/wg-quick"
            )
            settings_obj.wg_dir = settings_dict.get("wg_dir", "/etc/wireguard")
            settings_obj.peer_config_dir = settings_dict.get(
                "peer_config_dir", "/etc/wireguard"
            )
            return settings_obj
