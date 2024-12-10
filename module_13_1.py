import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for num in range(1, 6):
        await asyncio.sleep(num / power)
        print(f'Силач {name} поднял {num}-й шар')
    print(f'Силач {name} закончил соревнования')


async def start_tournament(participants):
    list_tasks = list()
    for i_participant in participants:
        list_tasks.append(asyncio.create_task(start_strongman(*i_participant)))
    for i_task in list_tasks:
        await i_task


participant1 = ['Pasha', 3]
participant2 = ['Denis', 4]
participant3 = ['Apollon', 5]
list_participants = [participant1, participant2, participant3]
asyncio.run(start_tournament(list_participants))