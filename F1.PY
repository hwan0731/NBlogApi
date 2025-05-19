import requests

def get_driver_standings(season='current'):
    url = f"http://ergast.com/api/f1/{season}/driverStandings.json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        standings_list = data['MRData']['StandingsTable']['StandingsLists']

        if standings_list:
            drivers = standings_list[0]['DriverStandings']
            for idx, driver in enumerate(drivers, 1):
                name = driver['Driver']['givenName'] + " " + driver['Driver']['familyName']
                points = driver['points']
                team = driver['Constructors'][0]['name']
                position = driver['position']
                print(f"{position}. {name} ({team}) - {points} pts")
        else:
            print("순위 정보가 없습니다.")
    else:
        print("API 요청 실패:", response.status_code)

if __name__ == "__main__":
    print("F1 드라이버 현재 순위")
    get_driver_standings()

