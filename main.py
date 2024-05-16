import os
import random
import time

red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
cyan = '\033[36m'
white = '\033[0m'

user_Todo_data = [['SR.NO', 'TASK', 'DUE DATE', 'IMP LEVEL'],
                  ['-----', '-----', '-----', '-----']]

# print(yellow,
#   '\nIN ONRDER TO GET PERFECT EXPERIENCE, MAKE SURE YOUR AREA OF CONSOLE OR TERMINAL IS BIG IN TERMS OF SIZE\n'
# )
# print(
#   '\nADVICE ---> full your console or terminal size atlest till run button\n',white
# )
# time.sleep(6)
# print('\nloading....')
# print('\nplease wait... till then read the instructions above ⬆️⬆️⬆️⬆️⬆️\n')
# # time.sleep(10)
# os.system('clear')
# print(user_Todo_data)
sr_no = 0
intro_only1 = True
iteratino = 0
while True:
  if intro_only1 is True:
    print(
        blue,
        '\n\n ----------------------> Welcome to ToDay Manager <------------------------------'
    )
    print(red, '                          -------------------------\n\n',
          white)
    intro_only1 = False
  # print(f'{white}')
  print()
  print()
  print()
  menu = input(
      '\nDo you want to add, view, edit or remove from the to do list 🤔 ---> '
  ).strip().lower()

  if menu == 'add':
    if iteratino >= 2:
      print(
          blue,
          '\n\n ----------------------> Welcome to ToDay Manager <-----------  -------------------'
      )
      print(red, '                          -------------------------\n\n  ',
            white)
    iteratino += 1
    sr_no += 1
    print(
        f'\n{red} currently Sr.no {sr_no} is going on. Make sure you fill number {sr_no} in sr.no section while adding task\n\n'
    )
    print(
        red,
        '\n😮😮 WARNING!!!! ---> while typing all requirements in one line please make sure to give spcase between sr.no, task, date, priority. PLEASE DO NOT PRESS ENTER while filling all till priority.\n'
    )
    print('or else your entry shall not be recorded properly😨', white)
    print(cyan)
    print('\n\n\n***************** instruction ****************')
    print(white)
    print(
        '\n\nEnter FIRST Sr.no (refer Sr.no from the top of warning statement line colored in red)'
    )
    print('\n\nSECOND enter Task name')
    print('\n\nTHIRD enter Due date')
    print('\n\nFOURTH enter IMPORTANT LEVEL')

    print(cyan)
    user_Todo_data.append(
        input(
            '\n\n\n-----> KINDLY READ INSTRUCTIONS FIRST. Pressenig space bar after every requirments in one line over here ---> '
        ).strip().capitalize().split())
    print(green, '\nThanks, this task has been added.', white)
    # time.sleep(2)
    # print('clearing..')
    # time.sleep(3)
    # os.system('clear')
#---------------------------------------------------------------
  elif menu == 'view':
    print(
        blue,
        '\n\n ----------------------> Welcome to ToDay Manager <------------------------------'
    )
    print(red, '                          -------------------------\n\n',
          white)
    print(purple)
    view_menu = input(
        "\n\nPress '1' for view all.\n\nPress '2' for view by Priority.\n\nenter the nubmer over here ----> "
    ).strip().lower()
    print()
    print()
    print()
    if view_menu == '1':
      for row in user_Todo_data:
        for iteam in row:
          print(f'{iteam:^20}', end=' | ')
        print()

    elif view_menu == '2':
      dicide_priority = input(
          "What's the level priority?\n\nPress 1 for low\n\nPress 2 for medium\n\nPress 3 for high)----> "
      ).strip().lower()
      if dicide_priority == '1':
        low_priority_found = False
        for row in user_Todo_data:
          for item in row:
            if item == 'low':
              low_priority_found = True
              print()
              print()
              print()
              for item in row:
                print(f'{item:^20}', end=' | ')
        if not low_priority_found:
          print(red, '\n\nThere is nothing in low priority 😑')

      elif dicide_priority == '2':
        no_medium = False
        for row in user_Todo_data:
          for item in row:
            if item == 'medium':
              no_medium = True
              print()
              print()
              print()
              for item in row:
                print(f'{item:^20}', end=' | ')
        if not no_medium:
          print(red, '\n\nThere is nothing in medium priority 😑')

      elif dicide_priority == '3':
        no_high = False
        for row in user_Todo_data:
          for item in row:
            if item == 'high':
              no_high = True
              print()
              print()
              print()
              for item in row:
                print(f'{item:^20}', end=' | ')
        if not no_high:
          print(red, '\n\nThere is nothing in high priority 😑')

    print(white)
#-------------------------------------------------------------------
  elif menu == 'edit':
    print(
        blue,
        '\n ----------------------> Welcome to ToDay Manager <------------------------------'
    )
    print(red, '                          -------------------------\n\n',
          white)
    print(yellow)
    for row in user_Todo_data:
      for item in row:
        print(item, end=' | ')
    edit_menu = input('\nWhat do you want to edit? ----> (CHOOSE BY TASK NAME)'
                      ).strip().capitalize()
    for row in user_Todo_data:
      for item in row:
        if edit_menu in item:
          # print(item)
          decide_edit = input(
              'what you want to edit from the above entry? ()----> ').strip(
              ).lower()
          for row in user_Todo_data:
            for item in row:
              if decide_edit in item:
                user_Todo_data.remove(decide_edit)
                new_entry = input(
                    "what you want to edit Task, Date or Priority? ----> "
                ).strip().lower()
                if new_entry == 'task':
                  user_Todo_data.append(
                      input('\nWhat is the task? ----> ').strip().capitalize())
                  print('successfully updated')
                elif new_entry == 'date':
                  user_Todo_data.append(
                      input(
                          '\nWhen it is due by? (date)----> ').strip().lower())
                  print('successfully updated')
                elif new_entry == 'priority':
                  user_Todo_data.append(
                      input(
                          '\nWhat is the Priority level? (low, medium or high) ----> '
                      ).strip().capitalize())
                  print('successfully updated')

  elif menu == 'remove':
    print(
        blue,
        '\n ----------------------> Welcome to ToDay Manager <------------------------------'
    )
    print(red, '                          -------------------------\n\n',
          white)
    print(blue)
    decide_remove = input(
        'which entry you want to remove? (choose by TASK NAME) ----> ').strip(
        ).lower()
    for row in user_Todo_data:
      for item in row:
        if decide_remove in item:
          user_Todo_data.remove(item)
          print('successfully removed')
          print("\nhere's the updated list\n")
          for row in user_Todo_data:
            for item in row:
              print(item, end=' | ')
        else:
          print(f"this entry {decide_remove} is not present in the todo list")

  else:
    print(red)
    print(
        'ERROR!!! please choose from the above option. Make sure your spelling is correct\n\n',
        white)
    continue

  print(white)
  print()
  print()
  print()
  exit_or_continue = input(
      'are you done with your Todo list? (yes or no)  ----> ').strip().lower()
  if exit_or_continue == 'yes':
    os.system('clear')
    print(
        green,
        "\nsee you in the next time\n\nhere's your final TOdo make sure to take a screenshot of it.👍"
    )
    print()
    print()
    print(white)
    for row in user_Todo_data:
      for iteam in row:
        print(f'{iteam:^20}', end=' | ')
      print()
    exit()
  else:
    print('\nclearing the history also stroing it in our cloud')
    # time.sleep(4)
    os.system('clear')
    continue
