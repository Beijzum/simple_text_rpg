## COMP1510TermProject

## Your name:

Jason Chow

## Your student number:

A00942129

## Your GitHub username:

Beijzum

## Instructions

- Best played in Terminal due to the clear() function.
- 1 , 2, 3, 4 are directions to move, and 5 shows the map.
- 6 shows the character's stats, and 7 shows the character's inventory.
- 8 saves the game, and 0 returns to the start menu
- You can visit the shop in the middle of the map to buy items and abilities.
- Enemies get stronger after the first two bosses!
- You can run away from a fight.
- You can use abilities and items.

## Spoilers! Quick walkthrough:

- First, you need to collect 2 special items from the top right corner and bottom left corner of the map.
- You can take these 2 special items to the bottom right area of the map.
- You will fight two more bosses and grab their equipment.
- The Final Boss room is in the bottom right. However, you need 2 special equipment to fight it.
- You can get these 2 special equipment from the top left and bottom right corners of the map.
- Good luck!

## Requirements:

| Requirement               | Where to find                                                                    |
|---------------------------|:---------------------------------------------------------------------------------|
| 5x5 Grid Map              | ![img_3.png](readme_pics/img_3.png)<br/>show_map() in exploration.py             |
| Character Dictionary      | ![img_4.png](readme_pics/img_4.png)<br/>make_character() in character.py         |
| Character Movement        | ![img_5.png](readme_pics/img_5.png)<br/>move_character() in exploration.py       |
| Encounter Challenges      | ![img_6.png](readme_pics/img_6.png)<br/>check_for_foes() in enemy.py             |
| Overcome Challenges       | ![img_7.png](readme_pics/img_7.png)<br/>combat_loop() in game().                 |
| Goal Achieved = Game Ends | ![img_8.png](readme_pics/img_8.png)<br/>check_win_condition() in exploration.py. |
| Leveling System           | ![img_9.png](readme_pics/img_9.png)<br/>level_up() in character.py               |
| Leveling Details          | ![img_10.png](readme_pics/img_10.png)<br/>battle_rewards() in loot.py            |
| Leveling Stats            | ![img_9.png](readme_pics/img_9.png)<br/>level_up() in character.py               |
| Final Boss                | ![img_11.png](readme_pics/img_11.png)<br/>game() in game.py                      |
| Stronger Enemies          | ![img_12.png](readme_pics/img_12.png)<br/>game() in game.py                      |
| Game Over                 | ![img_13.png](readme_pics/img_13.png)<br/>combat_loop() in game.py               |
| Immutable Data Structures | ![img_1.png](readme_pics/img_1.png)<br/>make_board() in exploration.py           |
| Mutable Data Structures   | ![img.png](readme_pics/img.png)<br/>learn_ability() in character.py              |
| Handling Exception Errors | ![img_2.png](readme_pics/img_2.png)<br/>load_game() in game.py                   |
| Minimized Scope, Objects  | ![img_4.png](readme_pics/img_4.png)<br/>make_character() in character.py         |
| Atomic Functions          | ![img_14.png](readme_pics/img_14.png)<br/>utility.py                             |
| Simple Flat Code          | ![img_15.png](readme_pics/img_15.png)<br/>get_user_choice() in game.py           |
| Dictionary Comprehension  | ![img_16.png](readme_pics/img_16.png)<br/>visit_shop() in loot.py                |
| if-elif-else Statements   | ![img_15.png](readme_pics/img_15.png)<br/>get_user_choice() in game.py           |
| while-loop                | ![img_17.png](readme_pics/img_17.png)<br/>combat_loop() in game.py               |
| Membership Operator       | ![img_18.png](readme_pics/img_18.png)<br/>battle_rewards() in loot.py            |
| Range Function            | ![img_1.png](readme_pics/img_1.png)<br/>make_board() in exploration.py           |
| Itertools                 | ![img_19.png](readme_pics/img_19.png)<br/>multi_strike() in combat.py            |
| Random Module             | ![img_6.png](readme_pics/img_6.png)<br/>check_for_foes() in enemy.py             |
| Function Annotations      | ![img_14.png](readme_pics/img_14.png)<br/>draw_box() in utility.py               |
| Doctests & Unit Tests     | ![img_20.png](readme_pics/img_20.png)<br/>Tests folder                           |
| F-string Usage            | ![img_21.png](readme_pics/img_21.png)<br/>enemy_attack() in combat.py            |        

## Notes:

Tests not done on the following:

- start_game(): I don't know how to test this function because it has many other function calls inside it.
- save_game(): Testing it saves an actual JSON file, which is not ideal for testing.
- load_game(): I don't know how to mock a JSON file, so I can't test this function.
- game(): It is too complicated to test due to the large amount of decisions and function calls.
- combat_loop(): It is too complicated to test due to the large amount of decisions and function calls.
- visit_shop(): It is too complicated to test due to the large amount of decisions and function calls.