import requests as request


earth = request.get("https://api.warframestat.us/pc/en/earthCycle")

earth_status = earth.status_code

if earth_status == 200:

    earth_data = earth.json()
    print("earth:")
    print(f"State: {earth_data['state']}")
    print(f"Time Left: {earth_data['timeLeft']}")
    print("")
else:
    print(f"status code: {earth.status_code}")
    print("")


cetus = request.get("https://api.warframestat.us/pc/en/cetusCycle")

cetus_status = cetus.status_code

if cetus_status == 200:

    cetus_data = cetus.json()
    print("Cetus:")
    print(f"State: {cetus_data['state']}")
    print(f"Time Left: {cetus_data['timeLeft']}")
    print("")
else:
    print(f"status code: {cetus.status_code}")
    print("")


vallis = request.get("https://api.warframestat.us/pc/en/vallisCycle")

vallis_status = vallis.status_code

if vallis_status == 200:

    vallis_data = vallis.json()
    print("Orb Vallis:")
    print(f"State: {vallis_data['state']}")
    print(f"Time Left: {vallis_data['timeLeft']}")
    print("")
else:
    print(f"status code: {vallis.status_code}")
    print("")


cambion = request.get("https://api.warframestat.us/pc/en/cambionCycle")

cambion_status = cambion.status_code

if cambion_status == 200:

    cambion_data = cambion.json()
    print("Cambion Drift:")
    print(f"State: {cambion_data['state']}")
    print(f"Time Left: {cambion_data['timeLeft']}")
    print("")
else:
    print(f"status code: {cambion.status_code}")
    print("")


zariman = request.get("https://api.warframestat.us/pc/en/zarimanCycle")

zariman_status = zariman.status_code

if zariman_status == 200:

    zariman_data = zariman.json()
    print("zariman:")
    print(f"State: {zariman_data['state']}")
    print(f"Time Left: {zariman_data['timeLeft']}")
    print("")
else:
    print(f"status code: {zariman.status_code}")
    print("")


duviri = request.get("https://api.warframestat.us/pc/en/duviriCycle")

duviri_status = duviri.status_code

if duviri_status== 200:

    duviri_data = duviri.json()

    print("Duviri:")
    for i, category in enumerate(duviri_data['choices']):
        if i == 1:
            print("\nDuviri SteelPath:")

        for choice in category['choices']:
            print(choice)

else:
    print(f"status code: {duviri.status_code}")
    print("")
