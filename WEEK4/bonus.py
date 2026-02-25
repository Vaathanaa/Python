class SportsLeague:
    def __init__(self):
        self.teams = {}  # team_name -> list of player dicts

    def add_team(self, team_name):
        if team_name not in self.teams:
            self.teams[team_name] = []
            print(f"Team '{team_name}' added.")
        else:
            print(f"Team '{team_name}' already exists.")

    def add_player(self, team_name, player_id, player_name, position):
        if team_name not in self.teams:
            print(f"Team '{team_name}' does not exist.")
            return

        # Check duplicate ID
        if any(p["id"] == player_id for p in self.teams[team_name]):
            print(f"Player ID {player_id} already exists in team '{team_name}'.")
            return

        self.teams[team_name].append({
            "id": player_id,
            "name": player_name,
            "position": position
        })
        print(f"Player '{player_name}' added to team '{team_name}'.")

    def view_team(self, team_name):
        if team_name not in self.teams:
            print(f"Team '{team_name}' does not exist.")
            return

        print(f"Team '{team_name}' players:")
        for p in self.teams[team_name]:
            print(f"ID: {p['id']}, Name: {p['name']}, Position: {p['position']}")

    def update_player(self, team_name, player_id, new_name=None, new_position=None):
        if team_name not in self.teams:
            print(f"Team '{team_name}' does not exist.")
            return

        for p in self.teams[team_name]:
            if p["id"] == player_id:
                if new_name:
                    p["name"] = new_name
                if new_position:
                    p["position"] = new_position
                print(f"Player ID {player_id} updated in team '{team_name}'.")
                return

        print("Player not found.")

    def remove_player(self, team_name, player_id):
        if team_name not in self.teams:
            print(f"Team '{team_name}' does not exist.")
            return

        for i, p in enumerate(self.teams[team_name]):
            if p["id"] == player_id:
                removed_name = p["name"]
                del self.teams[team_name][i]
                print(f"Player '{removed_name}' removed from team '{team_name}'.")
                return

        print("Player not found.")