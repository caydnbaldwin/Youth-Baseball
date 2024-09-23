def get_players():
    # get player name
    name = input('Enter player name: ')
    if not name:
        return None
    # get player age
    age = input('Enter player age: ')
    return name, int(age)


def get_teams():
    teams = []
    while True:
        # get player information
        team = get_players()
        if team is None:
            break
        # append player to team
        teams.append(team)
    return teams

def filter_teams(teams):
    bigs_team = []
    littles_team = []
    for name, age in teams:
        # append player to bigs team if player is older than 10
        if age > 10:
            bigs_team.append((name, age))
        # append player to littles team if player is younger than 10
        elif age <= 10:
            littles_team.append((name, age))
    return bigs_team, littles_team


def get_average_age(team):
    total_age = 0
    # sum the age
    for name, age in team:
        total_age += age
    # return the calculated average
    return round(total_age/len(team))


def get_youngest_age(team):
    youngest_age = None
    # get the youngest age
    for name, age in team:
        # replace the youngest age if the age is less than the youngest age
        if youngest_age is None or age < youngest_age:
            youngest_age = age
    return youngest_age


def get_oldest_age(team):
    oldest_age = None
    # get the oldest age
    for name, age in team:
        # replace the oldest age if the age is greater than the oldest age
        if oldest_age is None or age > oldest_age:
            oldest_age = age
    return oldest_age


def get_stats(team):
    # get the average, youngest, and oldest age from the teams
    average_age = get_average_age(team)
    youngest_age = get_youngest_age(team)
    oldest_age = get_oldest_age(team)
    return average_age, youngest_age, oldest_age


def print_report(stats, team):
    average_age, youngest_age, oldest_age = stats
    # print team information
    print(f'Total members: {len(team)}\n'
          f'Average age: {average_age}\n'
          f'Youngest age: {youngest_age}\n'
          f'Oldest age: {oldest_age}\n'
          f'Members')
    for name, age in team:
        print(f' - {name} {age}')


def print_teams(bigs_team, littles_team):
    # get the statistics for the teams
    bigs_team_stats = get_stats(bigs_team)
    littles_team_stats = get_stats(littles_team)
    # print the teams and their reports
    print('Team Bigs')
    print_report(bigs_team_stats, bigs_team)
    print('Team Littles')
    print_report(littles_team_stats, littles_team)


def main():
    # get all players for teams
    teams = get_teams()
    # filter teams by age
    bigs_team, littles_team = filter_teams(teams)
    # print information for the teams
    print_teams(bigs_team, littles_team)


if __name__ == '__main__':
    main()
