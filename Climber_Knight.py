from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.clock import Clock
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.slider import Slider
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.widget import Widget
import math
from kivy.uix.scrollview import ScrollView
from math import *


Window.size = (360, 640)

x = Window.width / 6
y = Window.height / 8

z = y - x

x_level = Window.width / 4
y_level = Window.height / 11.5

screens=ScreenManager()

class Coin(Image):
    def __init__(self):
        super().__init__()
        self.source= ('Design Screen/монетка.zip')
        self.source_2 =  ('Design Screen/check_coin.zip')
        self.anim_delay = .1
        self.keep_ratio = False


class Climbing(App, Screen):
    # Функция нажатия на кнопку Домой в меню
    def press_HOME(self, args):
        self.sm.current = 'first'
        self.sm.transition.duration = 0.5
        self.menu_image.y = y*8
        self.count = 0
        self.power = 0
        self.press_menu_continue()
        for i in self.count_screen[:]:
            i.remove_widget(self.menu_box)
            i.remove_widget(self.menu_image)

    # Функция нажатия на кнопку Play
    def press_ME(self, args):
        self.sm.current = 'character'
        self.sm.transition.direction = 'left'
        self.sm.transition.duration = 0.5

    # Функция возврата к первому экрану
    def press_RETURN(self, args):
        self.sm.current = 'first'
        self.sm.transition.direction = 'right'
        self.sm.transition.duration = 0.5

    def press_RETURN_TO_CHARACTER(self,args):
        self.sm.current = 'character'
        self.sm.transition.direction = 'right'
        self.sm.transition.duration = 0.5

    def press_RETURN_TO_ITEMS(self,args):
        self.sm.current = 'items'
        self.sm.transition.direction = 'right'
        self.sm.transition.duration = 0.5

    # Функция вызова меню Options
    def press_OPTIONS(self, args):
        self.sm.current = 'options'
        self.sm.transition.direction = 'left'
        self.sm.transition.duration = 0.5

    def press_TAP_TO_START(self, args):
        self.sm.current = 'Menu_select_level'
        self.intro_image.anim_loop = 1
        self.intro_image.anim_delay = .03
        self.sm.transition.duration = 0.5

    def press_SHOP_BUTTON(self, args):
        self.sm.current = 'items'
        self.sm.transition.duration = 0.5
        for i in self.count_screen[:]:
            i.remove_widget(self.menu_box)
            i.remove_widget(self.menu_image)

    def press_SHUES(self, args):
        self.sm.current = 'shues'
        self.sm.transition.duration = 0.5

    def press_CLOTHES(self, args):
        self.sm.current = 'clothes'
        self.sm.transition.duration = 0.5

    def press_UPGRADES(self, args):
        self.sm.current = 'upgrades'
        self.sm.transition.duration = 0.5

    def press_STORE(self, args):
        self.sm.current = 'store'
        self.sm.transition.duration = 0.5

    def press_change_skin(self, args):
        if self.screen_for_skins.current == 'four_skin':
            self.screen_for_skins.current = 'first_skin'
            self.screen_for_skins.transition.duration = 0.5
            self.count_skin = 0

        elif self.screen_for_skins.current == 'first_skin':
            self.screen_for_skins.current = 'second_skin'
            self.screen_for_skins.transition.duration = 0.5
            self.count_skin = 1

        elif self.screen_for_skins.current == 'second_skin':
            self.screen_for_skins.current = 'three_skin'
            self.screen_for_skins.transition.duration = 0.5
            self.count_skin = 2

        elif self.screen_for_skins.current == 'three_skin':
            self.screen_for_skins.current = 'four_skin'
            self.screen_for_skins.transition.duration = 0.5
            self.count_skin = 3

    def press_change_skin_for_game(self, args):
        for i in self.skins[:]:
            for a in range(3):
                if self.count_skin == a:
                    i = True
                else:
                    i = False

    def press_skin_button(self, args):
        self.sm.current = 'skin'
        self.sm.transition.duration = 0.5

    def start_level(self, *args):
        self.level_screen[self.level_count].add_widget(self.start_box)
        if self.level_count == 0:
            self.sm.current = 'First_level'
        if self.level_count == 1:
            self.sm.current = 'Second_level'

        if self.level_count == 2:
            self.sm.current = 'Three_level'

        if self.level_count == 3:
            self.sm.current = 'Four_level'
            self.animation_circle_frag()

        if self.level_count == 4:
            self.sm.current = 'Five_level'
            # self.animated_frag.cancel()
            self.animation_kick_frag()

        if self.level_count == 5:
            self.sm.current = 'Six_level'

        if self.level_count == 6:
            self.sm.current = 'Seven_level'

        if self.level_count == 7:
            self.sm.current = 'Eight_level'

        if self.level_count == 8:
            self.sm.current = 'Nine_level'

        if self.level_count == 9:
            self.sm.current = 'Ten_level'

    def start(self, *args):
        self.start_left = False
        self.one_hit = False

        self.words_collect_flag()
        self.down_number = 0
        self.static_number = 0
        self.level_start[self.level_count] = True
        self.level_screen[self.level_count].remove_widget(self.start_box)
        self.knight_image_boxes[self.level_count].remove_widget(self.knight_image_start[self.level_count])
        self.knight_image_start[self.level_count]=self.start_movie
        self.knight_image_start[self.level_count].anim_delay = 0.045
        self.knight_image_boxes[self.level_count].add_widget(self.knight_image_start[self.level_count])
        self.touch_down_button = Clock.schedule_once(self.touch_down, 5)

    def touch_down(self, *args):
        self.death = False
        self.knight_image_boxes[self.level_count].remove_widget(self.knight_image_start[self.level_count])
        self.knight_image_boxes[self.level_count].padding = (0,0,x,0)
        self.knight_image_walk[self.level_count] = self.walk_movie
        self.knight_image_boxes[self.level_count].add_widget(self.knight_image_walk[self.level_count])
        self.up_image = Clock.schedule_interval(self.up_up, .01)
        self.up_funct = Clock.schedule_interval(self.up_function, .01)
        self.level_screen[self.level_count].add_widget(self.swipe[self.level_count])
        if self.level_count >= 1:
            self.down_down()
        self.touch_down_button.cancel()

    def up_up(self, *args):
        self.climb_screen[self.level_count].y -= 2
        self.knight_image_boxes[self.level_count].y += 2
        self.knight_box[self.level_count].y += 2
        self.sky_box[self.level_count].y -= 0.2

    def up_function(self, *args):
        self.defeat()
        self.check_coin()
        self.win_level()
        self.frages_collide_screen()
        self.word_collect()



    def down_down(self, *args):
        self.random_down = Clock.schedule_interval(self.down_items, .01)

    def down_items(self, *args):
        if self.level_start[1] == True:
            if self.down_number < 3:
                self.frags_level_two_down[self.down_number].y -= 6
                self.frags_image_level_two_down[self.down_number].y -= 6

        if self.level_start[2] == True:
            if self.down_number < 1:
                self.frags_level_three_down[self.down_number].y -= 6
                self.frags_image_level_three_down[self.down_number].y -= 6

        if self.level_start[3] == True:
            if self.down_number < 1:
                self.frags_level_four_down[self.down_number].y -= 6
                self.frags_image_level_four_down[self.down_number].y -= 6

        if self.level_start[4] == True:
            if self.down_number < 1:
                self.frags_level_five_down[self.down_number].y -= 6
                self.frags_image_level_five_down[self.down_number].y -= 6

        if self.level_start[5] == True:
            if self.down_number < 1:
                self.frags_level_six_down[self.down_number].y -= 6
                self.frags_image_level_six_down[self.down_number].y -= 6

        if self.level_start[6] == True:
            if self.down_number < 1:
                self.frags_level_seven_down[self.down_number].y -= 6
                self.frags_image_level_seven_down[self.down_number].y -= 6

        if self.level_start[7] == True:
            if self.down_number < 1:
                self.frags_level_eight_down[self.down_number].y -= 6
                self.frags_image_level_eight_down[self.down_number].y -= 6

        if self.level_start[8] == True:
            if self.down_number < 1:
                self.frags_level_nine_down[self.down_number].y -= 6
                self.frags_image_level_nine_down[self.down_number].y -= 6

        if self.level_start[9] == True:
            if self.down_number < 1:
                self.frags_level_ten_down[self.down_number].y -= 6
                self.frags_image_level_ten_down[self.down_number].y -= 6


    def collide_down(self, *args):
        if self.down_number != 2:
            self.frags_image_down[self.level_count - 1][self.down_number].y = self.knight_image_boxes[
                                                                                  self.level_count].y + y * 28
            self.frags_box_down[self.level_count - 1][self.down_number].y = self.knight_image_boxes[
                                                                                self.level_count].y + y * 28
            self.down_number += 1

        if len(self.frags_image_down[self.level_count-1]) == self.down_number:
            self.random_down.cancel()

    def collide_down_death(self, *args):
        self.frags_image_down[self.level_count - 1][self.down_number].y = self.knight_image_boxes[
                                                                              self.level_count].y + y * 28
        self.frags_box_down[self.level_count - 1][self.down_number].y = self.knight_image_boxes[
                                                                            self.level_count].y + y * 28

    def frages_collide_screen(self, *args):
        if self.level_count < 10:
            if self.level_start[1] == True:
                if self.frags_down[self.level_count-1][self.down_number].top <= self.knight_image_boxes[self.level_count].y - y*2:
                    self.collide_down()

            if self.level_start[2] == True:
                if self.frags_down[self.level_count-1][0].top <= self.knight_image_boxes[self.level_count].y - y*2:
                    self.collide_down()

            if self.level_start[3] == True:
                if self.frags_down[self.level_count - 1][0].top <= self.knight_image_boxes[self.level_count].y - y * 2:
                    self.collide_down()

            if self.level_start[4] == True:
                if self.frags_down[self.level_count - 1][0].top <= self.knight_image_boxes[self.level_count].y - y * 2:
                    self.collide_down()

            if self.level_start[5] == True:
                if self.frags_down[self.level_count - 1][0].top <= self.knight_image_boxes[self.level_count].y - y * 2:
                    self.collide_down()

            if self.level_start[6] == True:
                if self.frags_down[self.level_count - 1][0].top <= self.knight_image_boxes[self.level_count].y - y * 2:
                    self.collide_down()

            if self.level_start[7] == True:
                if self.frags_down[self.level_count - 1][0].top <= self.knight_image_boxes[self.level_count].y - y * 2:
                    self.collide_down()

            if self.level_start[8] == True:
                if self.frags_down[self.level_count - 1][0].top <= self.knight_image_boxes[self.level_count].y - y * 2:
                    self.collide_down()

            if self.level_start[9] == True:
                if self.frags_down[self.level_count - 1][0].top <= self.knight_image_boxes[self.level_count].y - y * 2:
                    self.collide_down()

    def on_touch_down(self, touch, *args):
        if self.level_complete[self.level_count] == False:
            if self.swipe[self.level_count].value != 0:
                self.swipe[self.level_count].value = 0

    def on_touch_up(self, touch, *args):
        if self.level_complete[self.level_count]==False:
            if self.swipe[self.level_count].value == 0 and self.death == False:
                self.left = False

            if self.swipe[self.level_count].value < 0 and self.left == False and self.go_down == False and self.death == False:
                self.left = True
                self.start_left = True
                self.knight_left = Clock.schedule_interval(self.knight_move, .01)
                self.jumping()
                self.swipe[self.level_count].value = 0
            if self.right == False and self.death == False and self.start_sit == True:
                self.start_sit = False
                self.sit_up()
                self.swipe[self.level_count].value = 0


    def on_touch_move(self, touch, *args):
        if self.level_complete[self.level_count] == False:
            if self.swipe[self.level_count].value == 1 and self.left == False:
                self.start_sit = True
                self.sit_down()
                self.up_image.cancel()
                self.swipe[self.level_count].value = 0


    def check_coin(self, *args):
        if self.level_count < 5:
            for i in self.coins[self.level_count][:]:
                if self.knight_box_button[self.level_count].collide_widget(i):
                    i.anim_delay = 0.01
                    i.anim_loop = 1
                    i.source = i.source_2
                    self.timer = Clock.schedule_once(self.coin_count, .15)

    def coin_count(self, *args):
        for i in self.coins[self.level_count][:]:
            if self.knight_box_button[self.level_count].collide_widget(i):
                if self.level_count == 0:
                    for a in self.coin_boxes[self.level_count][:]:
                        a.remove_widget(i)

                    self.coins[self.level_count].remove(i)
                    self.coin_image_count = Label(
                        text=str(-(len(self.coins[self.level_count]) - len(self.coin_boxes[self.level_count]))),
                        font_size='30sp', color=(0, 0, 0, 1),
                        bold=(12))
                    self.coin_collect = int(-(len(self.coins[self.level_count]) - len(self.coin_boxes[self.level_count])))
                    self.timer.cancel()

                if self.level_count > 0:
                    for a in self.coin_boxes[self.level_count][:]:
                        a.remove_widget(i)
                    self.coins[self.level_count].remove(i)
                    self.coin_collect += 1
                    self.coin_image_count = Label(text=str(self.coin_collect), font_size='30sp', color=(0, 0, 0, 1),bold=(12))
                    self.timer.cancel()

    def win_level(self, *args):
        if self.climb_screen[self.level_count].y <= -y*20:
            self.level_complete[self.level_count] = True
            self.swipe[self.level_count].value = 0
            self.level_screen[self.level_count].remove_widget(self.swipe[self.level_count])
            self.up_image.cancel()
            self.up_funct.cancel()
            self.win_images = Clock.schedule_interval(self.win, .01)

    def win(self, *args):
        self.knight_image_boxes[self.level_count].remove_widget(self.knight_image_walk[self.level_count])
        self.knight_image_boxes[self.level_count].remove_widget(self.knight_image_jump[self.level_count])
        self.knight_image_boxes[self.level_count].remove_widget(self.knight_image_sit[self.level_count])
        self.knight_image_boxes[self.level_count].remove_widget(self.knight_image_sit_up[self.level_count])
        self.knight_image_boxes[self.level_count].remove_widget(self.knight_image_end[self.level_count])
        self.knight_image_end[self.level_count].anim_delay = 0.018
        self.knight_image_end[self.level_count] = self.end_movie
        self.knight_image_boxes[self.level_count].add_widget(self.knight_image_end[self.level_count])
        self.knight_box[self.level_count].y += 1
        if self.knight_box[self.level_count].y > self.wall_box[self.level_count].top*2.8:
            self.climb_screen[self.level_count].y -= 2
            self.sky_box[self.level_count].y -= 0.2
            if self.climb_screen[self.level_count].y <= -y*28:
                if self.level_count > 0:
                    self.random_down.cancel()

                self.win_images.cancel()
                self.update_images()
                self.remove_all_widgets()
                self.climb_screen[self.level_count].add_widget(self.maps_button_box[self.level_count])
                self.end_level_movie[self.level_count].anim_delay = .05
                self.end_level_movie[self.level_count].anim_loop = 1
                if self.level_count > 0:
                    self.maps_button_box_rel_coin_boxes[self.level_count-1].remove_widget(self.coin_image_count)
                    self.maps_button_box_levels_rel[self.level_count-1].remove_widget(self.level_try_count_image_box)

                self.maps_button_box_rel_coin_boxes[self.level_count].add_widget(self.coin_image_count)
                self.words_collect_flag_complete_menu()
                self.level_try_count_image = Label(text=str(self.level_try[self.level_count]), font_size='35sp',
                                                   color=[0, 0, 0, 1], bold=12)
                self.level_try_count_image_box = BoxLayout(padding=(x * 2.2, y, x * 1.4, y * 1.2))
                self.level_try_count_image_box.add_widget(self.level_try_count_image)
                self.maps_button_box_levels_rel[self.level_count].add_widget(self.level_try_count_image_box)
                if self.level_count == 5:
                    self.knight_level_six_complete_video.anim_loop = 1
                    self.knight_level_six_complete_video.anim_delay = 0.03
                self.level_start[self.level_count] = False
                self.win_levels = False
                self.level_complete[self.level_count] = True
                self.stars[0].anim_delay = -1


                self.level_count += 1

    def one_hit_knight(self, *args):
        if self.level_count >0:
            self.random_down.cancel()
        self.death = True
        if self.sit_once == True:
            self.sit_moving.cancel()
            self.start_sit = False
        self.up_image.cancel()
        if self.knight_image_boxes[self.level_count].x != 0:
            self.knight_image_boxes[self.level_count].x = 0
        self.knight_image_boxes[self.level_count].remove_widget(self.death_movie)
        self.level_screen[self.level_count].remove_widget(self.game_over_1)
        self.level_screen[self.level_count].remove_widget(self.game_over_repeat_button_box)
        self.level_screen[self.level_count].remove_widget(self.game_over_2)
        self.knight_image_boxes[self.level_count].remove_widget(self.knight_image_walk[self.level_count])
        self.knight_image_boxes[self.level_count].remove_widget(self.knight_image_jump[self.level_count])
        self.knight_image_boxes[self.level_count].remove_widget(self.knight_image_sit[self.level_count])
        self.knight_image_boxes[self.level_count].remove_widget(self.knight_image_sit_up[self.level_count])
        self.knight_image_boxes[self.level_count].remove_widget(self.knight_image_end[self.level_count])
        self.death_movie.anim_delay = 0.02
        self.knight_image_boxes[self.level_count].add_widget(self.death_movie)
        self.game_over_1.anim_delay = 0.02
        self.level_screen[self.level_count].add_widget(self.game_over_1)
        self.level_screen[self.level_count].add_widget(self.game_over_repeat_button_box)
        self.game_over_tic_tac = Clock.schedule_once(self.game_over_clock, .5)

    def game_over_clock(self, *args):
        self.level_screen[self.level_count].remove_widget(self.game_over_2)
        self.level_screen[self.level_count].remove_widget(self.game_over_1)
        self.level_screen[self.level_count].add_widget(self.game_over_2)
        self.game_over_tic_tac.cancel()


    def defeat(self, *args):
        if self.level_count == 0:
            if self.knight_box_button[self.level_count].collide_widget((self.frags[0])[0]):
                self.knight_box_button[self.level_count].x += x*20
                self.one_hit_knight()
            if self.knight_box_button[self.level_count].collide_widget((self.frags[0])[1]):
                self.knight_box_button[self.level_count].x += x * 20
                self.one_hit_knight()
            if self.knight_box_button[self.level_count].collide_widget((self.frags[0])[2]):
                self.knight_box_button[self.level_count].x += x * 20
                self.one_hit_knight()

        if self.level_count == 1:
            if self.knight_box_button[self.level_count].collide_widget((self.frags_down[0])[0]):
                self.knight_box_button[self.level_count].x += x * 20
                self.collide_down_death()
                self.one_hit_knight()
            if self.knight_box_button[self.level_count].collide_widget((self.frags_down[0])[1]):
                self.knight_box_button[self.level_count].x += x * 20
                self.collide_down_death()
                self.one_hit_knight()
            if self.knight_box_button[self.level_count].collide_widget((self.frags_down[0])[2]):
                self.knight_box_button[self.level_count].x += x * 20
                self.collide_down_death()
                self.one_hit_knight()

        if self.level_count > 1:
            #падающие враги
            if len(self.frags_down[self.level_count - 1]) == 1:
                if self.knight_box_button[self.level_count].collide_widget((self.frags_down[self.level_count-1])[0]):
                    self.collide_down_death()
                    self.one_hit_knight()
            if len(self.frags_down[self.level_count - 1]) > 1:
                if self.knight_box_button[self.level_count].collide_widget((self.frags_down[self.level_count-1])[0]):
                    self.collide_down_death()
                    self.one_hit_knight()
                if self.knight_box_button[self.level_count].collide_widget((self.frags_down[self.level_count-1])[1]):
                    self.collide_down_death()
                    self.one_hit_knight()
                if self.knight_box_button[self.level_count].collide_widget((self.frags_down[self.level_count-1])[2]):
                    self.collide_down_death()
                    self.one_hit_knight()

            #статичные враги
            if len(self.frags[self.level_count - 1]) == 1:
                if self.knight_box_button[self.level_count].collide_widget((self.frags[self.level_count-1])[0]):
                    self.knight_box_button[self.level_count].x += x * 20
                    self.one_hit_knight()

            if len(self.frags[self.level_count-1]) == 2:
                if self.knight_box_button[self.level_count].collide_widget((self.frags[self.level_count-1])[0]):
                    self.knight_box_button[self.level_count].x += x * 20
                    self.one_hit_knight()

                if self.knight_box_button[self.level_count].collide_widget((self.frags[self.level_count-1])[1]):
                    if self.level_count > 2:
                        self.knight_box_button[self.level_count].x += x * 20
                    self.one_hit_knight()

            if len(self.frags[self.level_count - 1]) == 3:
                if self.knight_box_button[self.level_count].collide_widget((self.frags[self.level_count-1])[0]):
                    self.knight_box_button[self.level_count].x += x * 20
                    self.one_hit_knight()
                if self.knight_box_button[self.level_count].collide_widget((self.frags[self.level_count-1])[1]):
                    self.knight_box_button[self.level_count].x += x * 20
                    self.one_hit_knight()
                if self.knight_box_button[self.level_count].collide_widget((self.frags[self.level_count-1])[2]):
                    self.knight_box_button[self.level_count].x += x * 20
                    self.one_hit_knight()

    def jumping(self, *args):
        self.jump_once = True
        self.knight_image_boxes[self.level_count].remove_widget(self.knight_image_jump[self.level_count])
        self.knight_image_boxes[self.level_count].remove_widget(self.knight_image_walk[self.level_count])
        self.knight_image_jump[self.level_count] = self.jump_movie
        self.knight_image_boxes[self.level_count].add_widget(self.knight_image_jump[self.level_count])
        self.knight_image_jump[self.level_count].anim_delay = 0.018
        self.knight_image_jump[self.level_count].anim_loop = 1

    def walking(self, *args):
        if self.start_left == False and self.start_right == False and self.left == False and self.right == True and self.death == False:
            self.knight_image_jump[self.level_count].anim_delay = -1
            self.knight_image_boxes[self.level_count].remove_widget(self.knight_image_walk[self.level_count])
            self.knight_image_boxes[self.level_count].remove_widget(self.knight_image_jump[self.level_count])
            self.knight_image_walk[self.level_count] = self.walk_movie
            self.knight_image_boxes[self.level_count].add_widget(self.knight_image_walk[self.level_count])

    def sit_down(self, *args):
        if self.right == True and self.death == False:
            self.sit_once = True
            self.go_down = True
            self.knight_box[self.level_count].x = self.knight_box[self.level_count].x + x
            self.knight_image_boxes[self.level_count].remove_widget(self.knight_image_walk[self.level_count])
            self.knight_image_sit[self.level_count] = self.sit_movie
            self.knight_image_boxes[self.level_count].add_widget(self.knight_image_sit[self.level_count])
            self.sit_move()
            self.knight_image_sit[self.level_count].anim_delay = 0.01
            self.knight_image_sit[self.level_count].anim_loop = 1
            self.right = False
            self.center_count = False

    def sit_move(self, *args):
        self.sit_moving = Clock.schedule_interval(self.sit_sit, .001)
    def sit_sit(self, *args):
        if self.knight_image_boxes[self.level_count].x < 40:
            self.level_screen[self.level_count].x -= 1
            self.knight_image_boxes[self.level_count].x += 2

    def sit_up_up_move(self, *args):
        self.sit_up_moving = Clock.schedule_interval(self.sit_up_up, .001)

    def sit_up_up(self, *args):
        if self.knight_image_boxes[self.level_count].x > 0:
            self.level_screen[self.level_count].x += 1
            self.knight_image_boxes[self.level_count].x -= 2

    def sit_up(self, *args):
        if self.center_count == False and self.death == False:
            self.sit_moving.cancel()
            self.go_up = True
            self.knight_image_boxes[self.level_count].remove_widget(self.knight_image_sit[self.level_count])
            self.knight_image_sit_up[self.level_count] = self.sit_up_movie
            self.knight_image_boxes[self.level_count].add_widget(self.knight_image_sit_up[self.level_count])
            self.sit_up_up_move()
            self.knight_image_sit_up[self.level_count].anim_delay = 0.01
            self.knight_image_sit_up[self.level_count].anim_loop = 1
            self.center_count = True
            self.move_up_again = Clock.schedule_once(self.move_again, .2)


    def move_again(self, *args):
        if self.go_up == True and self.death == False:
            self.sit_up_moving.cancel()
            self.knight_image_boxes[self.level_count].x = 0
            self.level_screen[self.level_count].x = 0
            self.up_image()
            self.knight_box[self.level_count].x = self.knight_box[self.level_count].x - x
            self.right = True
            self.knight_image_sit[self.level_count].anim_delay = -1
            self.knight_image_sit_up[self.level_count].anim_delay = -1
            self.knight_image_boxes[self.level_count].remove_widget(self.knight_image_sit_up[self.level_count])
            self.knight_image_walk[self.level_count] = self.walk_movie
            self.knight_image_boxes[self.level_count].add_widget(self.knight_image_walk[self.level_count])
            self.go_up = False
            self.go_down = False
            self.move_up_again.cancel()

    def knight_move(self, args):
        if self.start_left == True and self.death == False:
            self.level_screen[self.level_count].x += 1**1.2

            self.knight_box[self.level_count].x -= 2**1.2
            self.knight_box[self.level_count].y += 0.8**1.2
            self.knight_image_boxes[self.level_count].x -= 2

        if self.knight_box[self.level_count].x <= self.first_level_screen_child.x - x*2:
            self.start_left = False
            self.start_right = True

        if self.start_right == True and self.death == False:
            self.level_screen[self.level_count].x -= 1 ** 1.2
            self.knight_box[self.level_count].x += 2**1.2
            self.knight_box[self.level_count].y -= 0.8**1.2
            self.knight_image_boxes[self.level_count].x += 2

        if self.knight_box[self.level_count].x > 0 and self.death == False:
            self.knight_left.cancel()
            self.start_right = False
            self.left = False
            self.walking()

    def return_maps(self, *args):
        self.sm.current = 'Map'
        self.sm.transition.duration = 0.5
        self.scroll_screen.remove_widget(self.maps_image_rel)
        self.maps_image_rel.remove_widget(self.maps_image[self.level_count - 2])
        self.maps_image_rel.remove_widget(self.button_boxes[self.level_count - 2])
        self.maps_image_rel.remove_widget(self.maps_shadow_image[self.level_count - 2])

        self.maps_image_rel.remove_widget(self.stars_box[self.level_count-2])
        self.stars_box[self.level_count-2].remove_widget(self.stars[0])

        self.maps_image_rel.add_widget(self.maps_image[self.level_count-1])
        self.maps_image_rel.add_widget(self.button_boxes[self.level_count-1])
        self.maps_image_rel.add_widget(self.maps_shadow_image[self.level_count - 1])
        self.stars[0].anim_delay = 0.05
        self.stars[0].anim_loop = 1
        self.stars_box[self.level_count-1].add_widget(self.stars[0])

        self.maps_image_rel.add_widget(self.stars_box[self.level_count-1])

        self.scroll_screen.add_widget(self.maps_image_rel)


    def animation_circle_frag(self, *args):
        self.animated_frag = Clock.schedule_interval(self.frag_circle, .01)

    def frag_circle(self, *args):
        self.climb_screen_level_four.remove_widget(self.animation_frag_box_level_four)
        self.tangle_text_but -= math.pi/270
        self.animation_frag_box_level_four.center_x = x*1.5 * cos(self.tangle_text_but)
        self.animation_frag_box_level_four.center_y = y*1.2 * sin(self.tangle_text_but)
        self.climb_screen_level_four.add_widget(self.animation_frag_box_level_four)

    def animation_kick_frag(self, *args):
        self.animated_kick_frag = Clock.schedule_interval(self.frag_kick, .01)

    def frag_kick(self, *args):
        if self.level_count == 4:
            if self.frag_kick_image[0].x < x*2.1  and self.frag_kick_image[0].x > -x*2 and self.frag_kick_left == False:
                self.frag_kick_image[0].x -= 1.5
                self.frag_kick_right = False

            if self.frag_kick_image[0].x == -x*2 and self.frag_kick_right == False:
                self.frag_kick_left = True

            if self.frag_kick_left == True and self.frag_kick_right == False:
                self.frag_kick_image[0].x += 1.5

            if self.frag_kick_image[0].x == x * 2 and self.frag_kick_right == False:
                self.frag_kick_left = False
                self.frag_kick_image[0].x -= 1.5

        if self.level_count == 5:
            for i in self.frag_kick_image[1:3]:
                if i.x < x * 2.1 and i.x > -x * 2 and self.frag_kick_left == False:
                    i.x -= 1.5
                    self.frag_kick_right = False

                if i.x == -x * 2 and self.frag_kick_right == False:
                    self.frag_kick_left = True

                if self.frag_kick_left == True and self.frag_kick_right == False:
                    i.x += 1.5

                if i.x == x * 2 and self.frag_kick_right == False:
                    self.frag_kick_left = False
                    i.x -= 1.5
        if self.level_count == 6:
            for i in self.frag_kick_image[3:5]:
                if i.x < x * 2.1 and i.x > -x * 2 and self.frag_kick_left == False:
                    i.x -= 1.5
                    self.frag_kick_right = False

                if i.x == -x * 2 and self.frag_kick_right == False:
                    self.frag_kick_left = True

                if self.frag_kick_left == True and self.frag_kick_right == False:
                    i.x += 1.5

                if i.x == x * 2 and self.frag_kick_right == False:
                    self.frag_kick_left = False
                    i.x -= 1.5

        if self.level_count == 7:
            for i in self.frag_kick_image[5:7]:
                if i.x < x * 2.1 and i.x > -x * 2 and self.frag_kick_left == False:
                    i.x -= 1.5
                    self.frag_kick_right = False

                if i.x == -x * 2 and self.frag_kick_right == False:
                    self.frag_kick_left = True

                if self.frag_kick_left == True and self.frag_kick_right == False:
                    i.x += 1.5

                if i.x == x * 2 and self.frag_kick_right == False:
                    self.frag_kick_left = False
                    i.x -= 1.5

        if self.level_count == 8:
            for i in self.frag_kick_image[7:9]:
                if i.x < x * 2.1 and i.x > -x * 2 and self.frag_kick_left == False:
                    i.x -= 1.5
                    self.frag_kick_right = False

                if i.x == -x * 2 and self.frag_kick_right == False:
                    self.frag_kick_left = True

                if self.frag_kick_left == True and self.frag_kick_right == False:
                    i.x += 1.5

                if i.x == x * 2 and self.frag_kick_right == False:
                    self.frag_kick_left = False
                    i.x -= 1.5
        if self.level_count == 9:
            for i in self.frag_kick_image[9:11]:
                if i.x < x * 2.1 and i.x > -x * 2 and self.frag_kick_left == False:
                    i.x -= 1.5
                    self.frag_kick_right = False

                if i.x == -x * 2 and self.frag_kick_right == False:
                    self.frag_kick_left = True

                if self.frag_kick_left == True and self.frag_kick_right == False:
                    i.x += 1.5

                if i.x == x * 2 and self.frag_kick_right == False:
                    self.frag_kick_left = False
                    i.x -= 1.5

    def word_collect(self, *args):
        if self.knight_box_button[self.level_count].collide_widget(
                (self.words_knight[self.level_count])) and self.level_count < 6:
            self.words_knight[self.level_count].x += x * 20
            self.level_screen[self.level_count].remove_widget(self.Knight_letter[self.level_count])
            self.level_screen[self.level_count].add_widget(self.Knight_letter[self.level_count])
            self.word_flags[self.level_count] = True

        if self.knight_box_button[self.level_count].collide_widget(
                (self.words_knight[self.level_count])) and self.level_count >= 6:
            self.words_knight[self.level_count].x += x * 20
            self.level_screen[self.level_count].remove_widget(self.Lord_letter[self.level_count-6])
            self.level_screen[self.level_count].add_widget(self.Lord_letter[self.level_count-6])
            self.word_flags_lord[self.level_count-6] = True

    def words_collect_flag(self, *args):
        self.words_sum = 0
        if self.level_count < 6:
            for i in self.word_flags[:]:
                if i == False:
                    self.maps_button_box_rel_letter_boxes[self.level_count].remove_widget(
                        self.Knight_box_letter_empty[self.words_sum])
                    self.maps_button_box_rel_letter_boxes[self.level_count - 1].remove_widget(
                        self.Knight_box_letter_empty[self.words_sum])
                    self.level_screen[self.level_count].remove_widget(self.Knight_box_letter_empty[self.words_sum])
                    self.level_screen[self.level_count-1].remove_widget(self.Knight_box_letter_empty[self.words_sum])
                    self.level_screen[self.level_count].add_widget(self.Knight_box_letter_empty[self.words_sum])
                    self.words_sum += 1
                if i == True:
                    if self.level_count > 0:
                        self.Knight_letter[self.words_sum].remove_widget(self.Knight_letter_images[self.words_sum])
                        self.maps_button_box_rel_letter_boxes[self.level_count-1].remove_widget(
                            self.Knight_letter_images[self.words_sum])
                        self.Knight_letter[self.words_sum].add_widget(self.Knight_letter_images[self.words_sum])
                    self.level_screen[self.level_count-1].remove_widget(self.Knight_letter[self.words_sum])
                    self.level_screen[self.level_count].remove_widget(self.Knight_letter[self.words_sum])
                    self.level_screen[self.level_count].add_widget(self.Knight_letter[self.words_sum])
                    self.words_sum += 1

        if self.level_count >= 6:
            for i in self.word_flags_lord[:]:
                if i == False:
                    self.maps_button_box_rel_letter_boxes[self.level_count].remove_widget(
                        self.Lord_box_letter_empty[self.words_sum])
                    self.maps_button_box_rel_letter_boxes[self.level_count - 1].remove_widget(
                        self.Lord_box_letter_empty[self.words_sum])
                    self.level_screen[self.level_count].remove_widget(self.Lord_box_letter_empty[self.words_sum])
                    self.level_screen[self.level_count-1].remove_widget(self.Lord_box_letter_empty[self.words_sum])
                    self.level_screen[self.level_count].add_widget(self.Lord_box_letter_empty[self.words_sum])
                    self.words_sum += 1
                if i == True:
                    if self.level_count > 0:
                        self.Lord_letter[self.words_sum].remove_widget(self.Lord_letter_images[self.words_sum])
                        self.maps_button_box_rel_letter_boxes[self.level_count-1].remove_widget(
                            self.Lord_letter_images[self.words_sum])
                        self.Lord_letter[self.words_sum].add_widget(self.Lord_letter_images[self.words_sum])
                    self.level_screen[self.level_count-1].remove_widget(self.Lord_letter[self.words_sum])
                    self.level_screen[self.level_count].remove_widget(self.Lord_letter[self.words_sum])
                    self.level_screen[self.level_count].add_widget(self.Lord_letter[self.words_sum])
                    self.words_sum += 1



    def words_collect_flag_complete_menu(self, *args):
        self.words_summ = 0
        if self.level_count < 6:
            for i in self.word_flags[:]:
                if i == False:
                    self.level_screen[self.level_count].remove_widget(self.Knight_box_letter_empty[self.words_summ])
                    self.level_screen[self.level_count - 1].remove_widget(self.Knight_box_letter_empty[self.words_summ])
                    self.maps_button_box_rel_letter_boxes[self.level_count-1].remove_widget(
                        self.Knight_box_letter_empty[self.words_summ])
                    self.maps_button_box_rel_letter_boxes[self.level_count].remove_widget(
                        self.Knight_box_letter_empty[self.words_summ])
                    self.maps_button_box_rel_letter_boxes[self.level_count].add_widget(
                        self.Knight_box_letter_empty[self.words_summ])
                    self.words_summ += 1
                if i == True:
                    self.level_screen[self.level_count-1].remove_widget(self.Knight_letter[self.words_summ])
                    self.level_screen[self.level_count].remove_widget(self.Knight_letter[self.words_summ])
                    self.Knight_letter[self.words_summ].remove_widget(self.Knight_letter_images[self.words_summ])
                    self.maps_button_box_rel_letter_boxes[self.level_count].add_widget(self.Knight_letter_images[self.words_summ])
                    self.words_summ += 1

        if self.level_count >= 6:
            for i in self.word_flags_lord[:]:
                if i == False:
                    self.level_screen[self.level_count].remove_widget(self.Lord_box_letter_empty[self.words_summ])
                    self.level_screen[self.level_count - 1].remove_widget(self.Lord_box_letter_empty[self.words_summ])
                    self.maps_button_box_rel_letter_boxes[self.level_count-1].remove_widget(
                        self.Lord_box_letter_empty[self.words_summ])
                    self.maps_button_box_rel_letter_boxes[self.level_count].remove_widget(
                        self.Lord_box_letter_empty[self.words_summ])
                    self.maps_button_box_rel_letter_boxes[self.level_count].add_widget(
                        self.Lord_box_letter_empty[self.words_summ])
                    self.words_summ += 1
                if i == True:
                    self.level_screen[self.level_count-1].remove_widget(self.Lord_letter[self.words_summ])
                    self.level_screen[self.level_count].remove_widget(self.Lord_letter[self.words_summ])
                    self.Lord_letter[self.words_summ].remove_widget(self.Lord_letter_images[self.words_summ])
                    self.maps_button_box_rel_letter_boxes[self.level_count].add_widget(self.Lord_letter_images[self.words_summ])
                    self.words_summ += 1


    def update_images(self, *args):
        self.down_number = 0
        self.start_movie = Image(source=('Design Screen/start.zip'), anim_delay=-1, allow_stretch=True,
              keep_ratio=False,  anim_loop=1)
        self.jump_movie = Image(source=('Design Screen/jump.zip'), anim_delay=-1,
              keep_ratio=False, anim_loop=1)
        self.end_movie = Image(source=('Design Screen/end.zip'), anim_delay=-1,
                                                keep_ratio=False, anim_loop=1)
        self.walk_movie = Image(source=('Design Screen/walk.zip'), anim_delay=0.018,
                                                 keep_ratio=False)
        self.sit_movie = Image(source=('Design Screen/sit.zip'), anim_delay=-1,
                               keep_ratio=False)
        self.sit_up_movie = Image(source=('Design Screen/sit_up.zip'), anim_delay=-1,
                                  keep_ratio=False)
        self.shadow = Image(source=('Design Screen/shadow.zip'), anim_delay=-1, allow_stretch=True,
                                 keep_ratio=False, anim_loop = 1)
        self.game_over_1 = Image(source=('Design Screen/game_over_1.zip'), anim_delay=-1,
                                 keep_ratio=False, anim_loop=1)
        self.game_over_2 = self.game_over_2 = self.game_over_2 = Image(source=('Design Screen/game_over_2.zip'), anim_delay=0.05,
                                 keep_ratio=False)
        self.death_movie = Image(source=('Design Screen/death.zip'), anim_delay=-1,
                               keep_ratio=False, anim_loop=1, allow_stretch=True)
        self.frags_animation_level_four = Widget()


    def repeat_level(self, *args):

        if self.word_flags[self.level_count] == True:
            self.words_knight[self.level_count].x -= x * 20
            self.level_screen[self.level_count].remove_widget(self.Knight_letter[self.level_count])
            self.word_flags[self.level_count] = False

        if self.climb_screen[self.level_count].y < -y*20:
            self.win_images.cancel()

        self.go_up = False
        self.go_down = False

        if self.sit_once == True:
            self.sit_moving.cancel()
            self.sit_up_moving.cancel()
        if self.jump_once == True:
            self.knight_left.cancel()
            self.start_right = False

            self.start_left = False

        self.left = False
        self.right = True

        self.level_try[self.level_count] += 1
        self.tangle_text_but = 89.0
        self.remove_all_widgets()
        self.update_images()
        self.shadow.anim_delay = 0.05

        self.level_screen[self.level_count].add_widget(self.shadow)
        self.climb_screen[self.level_count].y = 0
        self.up_funct.cancel()
        self.up_image.cancel()

        self.timer_load_level = Clock.schedule_once(self.load_repeat_level, 1)
        self.knight_image_boxes[self.level_count].y = 0
        self.knight_image_boxes[self.level_count].x = 0
        self.knight_box[self.level_count].y = 0
        self.knight_box[self.level_count].x = 0
        self.sky_box[self.level_count].y = 0

        if self.level_count != 0:
            for i in range(3):
                self.frags_image_down[self.level_count - 1][self.down_number].y = self.knight_image_boxes[
                                                                                      self.level_count].y + y * 28
                self.frags_box_down[self.level_count - 1][self.down_number].y = self.knight_image_boxes[
                                                                                    self.level_count].y + y * 28

        if self.level_count == 3:
            self.animation_frag_image_box_level_four.add_widget(self.frags_animation_level_four)


    def remove_all_widgets(self, *args):
        self.knight_image_boxes[self.level_count].remove_widget(self.death_movie)
        self.level_screen[self.level_count].remove_widget(self.game_over_1)
        self.level_screen[self.level_count].remove_widget(self.game_over_2)
        self.level_screen[self.level_count].remove_widget(self.game_over_repeat_button_box)
        self.level_screen[self.level_count].remove_widget(self.swipe[self.level_count])
        self.level_screen[self.level_count].remove_widget(self.shadow)
        self.animation_frag_image_box_level_four.remove_widget(self.frags_animation_level_four)

    def load_repeat_level(self, *args):
        self.start()
        self.timer_load_level.cancel()


    def build(self):

        self.death = False

        # все анимации в игре


        self.bang_movie = Image(source=('Design Screen/check_coin.zip'), anim_delay=-1, allow_stretch=True,
                                 keep_ratio=False, anim_loop = 1)

        self.shadow = Image(source=('Design Screen/shadow.zip'), anim_delay=-1, allow_stretch=True,
                                 keep_ratio=False, anim_loop = 1)

        self.game_over_1 = Image(source=('Design Screen/game_over_1.zip'), anim_delay=-1,
                                 keep_ratio=False, anim_loop=1)

        self.game_over_2 = self.game_over_2 = Image(source=('Design Screen/game_over_2.zip'), anim_delay=0.05,
                                 keep_ratio=False)

        self.game_over_repeat_button_box = BoxLayout(padding = (x*4, y*4, x, y*3))

        self.game_over_repeat_button_box.add_widget(Button(on_press = self.repeat_level, background_color = (0,0,0,0)))

        self.start_movie = Image(source=('Design Screen/start.zip'), anim_delay=-1, allow_stretch=True,
              keep_ratio=False,  anim_loop=1)

        self.jump_movie = Image(source=('Design Screen/jump.zip'), anim_delay=-1,
              keep_ratio=False)

        self.end_movie = Image(source=('Design Screen/end.zip'), anim_delay=-1,
                                                keep_ratio=False, anim_loop=1)

        self.walk_movie =Image(source=('Design Screen/walk.zip'), anim_delay=0.018, allow_stretch=False,
                                                 keep_ratio=False)

        self.sit_movie = Image(source=('Design Screen/sit.zip'), anim_delay=-1,
                               keep_ratio=False)

        self.sit_up_movie = Image(source=('Design Screen/sit_up.zip'), anim_delay=-1,
                                  keep_ratio=False)

        self.death_movie =  Image(source=('Design Screen/death.zip'), anim_delay=-1,
                               keep_ratio=False, anim_loop=1, allow_stretch=True)



        # количество попыток прохождения уровня
        self.level_try_level_one = 0
        self.level_try_level_two = 0
        self.level_try_level_three = 0
        self.level_try_level_four = 0
        self.level_try_level_five = 0
        self.level_try_level_six = 0
        self.level_try_level_seven = 0
        self.level_try_level_eight = 0
        self.level_try_level_nine = 0
        self.level_try_level_ten = 0

        self.level_try_count_image_box = BoxLayout(padding=(x * 2.2, y, x * 1.4, y * 1.2))

        #сбор букв - флаги
        self.K_collect = False
        self.N_collect = False
        self.I_collect = False
        self.G_collect = False
        self.H_collect = False
        self.T_collect = False
        self.L_collect = False
        self.O_collect = False
        self.R_collect = False
        self.D_collect = False

        self.word_sum = 0
        self.word_count = 0
        self.coin_collect = 0

        # флаги движения
        self.go_up = False
        self.go_down = False
        self.left = False
        self.left_count = False
        self.center_count = True
        self.right = True
        self.start_levels = False
        self.hit_count = 0
        self.start_left = False
        self.start_right = False
        self.sit_once = False
        self.jump_once = False

        self.frag_kick_right = False
        self.frag_kick_left = False
        self.win_levels = False

        #меню в конце каждого уровня

        self.maps_button_box_level_one =  BoxLayout(padding=(0, -y*27, 0, y*31))
        self.maps_button_box_level_one_rel = RelativeLayout()
        self.end_level_movie_level_one = Image(source=('Design Screen/logo.zip'), anim_delay= 1)
        self.maps_button_box_level_one_rel.add_widget(self.end_level_movie_level_one)
        self.maps_button_box_level_one_rel_box = BoxLayout(padding = (x*3, y*3, x, 0))
        self.maps_button_box_level_one_rel_coin_box = BoxLayout(padding=(x*2.2, y, x*1.4, 0))
        self.maps_button_box_rel_letter_boxes_level_one = AnchorLayout(padding=(x*1.5, 0, x * 1.4, y*1.5))
        self.next_level_button_level_one = Button(on_press=self.return_maps, background_color = (255,255,0, 0))
        self.maps_button_box_level_one_rel_box.add_widget(self.next_level_button_level_one)
        self.maps_button_box_level_one_rel.add_widget(self.maps_button_box_level_one_rel_coin_box)
        self.maps_button_box_level_one_rel.add_widget(self.maps_button_box_level_one_rel_box)
        self.maps_button_box_level_one_rel.add_widget(self.maps_button_box_rel_letter_boxes_level_one)
        self.maps_button_box_level_one.add_widget(self.maps_button_box_level_one_rel)

        self.maps_button_box_level_two = BoxLayout(padding=(0, -y*27, 0, y*31))
        self.maps_button_box_level_two_rel = RelativeLayout()
        self.end_level_movie_level_two = Image(source=('Design Screen/logo.zip'), anim_delay=-1)
        self.maps_button_box_level_two_rel.add_widget(self.end_level_movie_level_two)
        self.maps_button_box_level_two_rel_box = BoxLayout(padding=(x*3, y*3, x, 0))
        self.maps_button_box_level_two_rel_coin_box = BoxLayout(padding=(x*2.2, y, x*1.4, 0))
        self.next_level_button_level_two = Button(on_press=self.return_maps, background_color=(255, 255, 0, 0))
        self.maps_button_box_level_two_rel_box.add_widget(self.next_level_button_level_two)
        self.maps_button_box_level_two_rel.add_widget(self.maps_button_box_level_two_rel_coin_box)
        self.maps_button_box_level_two_rel.add_widget(self.maps_button_box_level_two_rel_box)
        self.maps_button_box_rel_letter_boxes_level_two = AnchorLayout(padding=(x * 1.5, 0, x * 1.4, y*1.5))
        self.maps_button_box_level_two_rel.add_widget(self.maps_button_box_rel_letter_boxes_level_two)
        self.maps_button_box_level_two.add_widget(self.maps_button_box_level_two_rel)

        self.maps_button_box_level_three = BoxLayout(padding=(0, -y*27, 0, y*31))
        self.maps_button_box_level_three_rel = RelativeLayout()
        self.end_level_movie_level_three = Image(source=('Design Screen/logo.zip'), anim_delay=-1)
        self.maps_button_box_level_three_rel.add_widget(self.end_level_movie_level_three)
        self.maps_button_box_level_three_rel_box = BoxLayout(padding=(x*3, y*3, x, 0))
        self.maps_button_box_level_three_rel_coin_box = BoxLayout(padding=(x*2.2, y, x*1.4, 0))
        self.next_level_button_level_three = Button(on_press=self.return_maps, background_color=(255, 255, 0, 0))
        self.maps_button_box_level_three_rel_box.add_widget(self.next_level_button_level_three)
        self.maps_button_box_level_three_rel.add_widget(self.maps_button_box_level_three_rel_coin_box)
        self.maps_button_box_level_three_rel.add_widget(self.maps_button_box_level_three_rel_box)
        self.maps_button_box_rel_letter_boxes_level_three = AnchorLayout(padding=(x * 1.5, 0, x * 1.4, y*1.5))
        self.maps_button_box_level_three_rel.add_widget(self.maps_button_box_rel_letter_boxes_level_three)
        self.maps_button_box_level_three.add_widget(self.maps_button_box_level_three_rel)

        self.maps_button_box_level_four = BoxLayout(padding=(0, -y*27, 0, y*31))
        self.maps_button_box_level_four_rel = RelativeLayout()
        self.end_level_movie_level_four = Image(source=('Design Screen/logo.zip'), anim_delay=-1)
        self.maps_button_box_level_four_rel.add_widget(self.end_level_movie_level_four)
        self.maps_button_box_level_four_rel_box = BoxLayout(padding=(x*3, y*3, x, 0))
        self.maps_button_box_level_four_rel_coin_box = BoxLayout(padding=(x*2, y, x*1.4, 0))
        self.next_level_button_level_four = Button(on_press=self.return_maps, background_color=(255, 255, 0, 0))
        self.maps_button_box_level_four_rel_box.add_widget(self.next_level_button_level_four)
        self.maps_button_box_level_four_rel.add_widget(self.maps_button_box_level_four_rel_coin_box)
        self.maps_button_box_level_four_rel.add_widget(self.maps_button_box_level_four_rel_box)
        self.maps_button_box_rel_letter_boxes_level_four = AnchorLayout(padding=(x * 1.5, 0, x * 1.4, y*1.5))
        self.maps_button_box_level_four_rel.add_widget(self.maps_button_box_rel_letter_boxes_level_four)
        self.maps_button_box_level_four.add_widget(self.maps_button_box_level_four_rel)

        self.maps_button_box_level_five = BoxLayout(padding=(0, -y*27, 0, y*31))
        self.maps_button_box_level_five_rel = RelativeLayout()
        self.end_level_movie_level_five = Image(source=('Design Screen/logo.zip'), anim_delay=-1)
        self.maps_button_box_level_five_rel.add_widget(self.end_level_movie_level_five)
        self.maps_button_box_level_five_rel_box = BoxLayout(padding=(x*3, y*3, x, 0))
        self.maps_button_box_level_five_rel_coin_box = BoxLayout(padding=(x*2.2, y, x*1.4, 0))
        self.next_level_button_level_five = Button(on_press=self.return_maps, background_color=(255, 255, 0, 0))
        self.maps_button_box_level_five_rel_box.add_widget(self.next_level_button_level_five)
        self.maps_button_box_level_five_rel.add_widget(self.maps_button_box_level_five_rel_coin_box)
        self.maps_button_box_level_five_rel.add_widget(self.maps_button_box_level_five_rel_box)
        self.maps_button_box_rel_letter_boxes_level_five = AnchorLayout(padding=(x * 1.5, 0, x * 1.4, y*1.5))
        self.maps_button_box_level_five_rel.add_widget(self.maps_button_box_rel_letter_boxes_level_five)
        self.maps_button_box_level_five.add_widget(self.maps_button_box_level_five_rel)

        self.maps_button_box_level_six = BoxLayout(padding=(0, -y * 27, 0, y * 31))
        self.maps_button_box_level_six_rel = RelativeLayout()
        self.end_level_movie_level_six = Image(source=('Design Screen/logo.zip'), anim_delay=-1)
        self.maps_button_box_level_six_rel.add_widget(self.end_level_movie_level_six)
        self.maps_button_box_level_six_rel_box = BoxLayout(padding=(x * 3, y * 3, x, 0))
        self.maps_button_box_level_six_rel_coin_box = BoxLayout(padding=(x * 2.2, y, x * 1.4, 0))
        self.next_level_button_level_six = Button(on_press=self.return_maps, background_color=(255, 255, 0, 0))
        self.maps_button_box_level_six_rel_box.add_widget(self.next_level_button_level_six)
        self.maps_button_box_level_six_rel.add_widget(self.maps_button_box_level_six_rel_coin_box)
        self.maps_button_box_level_six_rel.add_widget(self.maps_button_box_level_six_rel_box)
        self.maps_button_box_rel_letter_boxes_level_six = AnchorLayout(padding=(x * 1.5, 0, x * 1.4, y * 1.5))
        self.maps_button_box_level_six_rel.add_widget(self.maps_button_box_rel_letter_boxes_level_six)
        self.maps_button_box_level_six.add_widget(self.maps_button_box_level_six_rel)

        self.maps_button_box_level_seven = BoxLayout(padding=(0, -y * 27, 0, y * 31))
        self.maps_button_box_level_seven_rel = RelativeLayout()
        self.end_level_movie_level_seven = Image(source=('Design Screen/logo.zip'), anim_delay=-1)
        self.maps_button_box_level_seven_rel.add_widget(self.end_level_movie_level_seven)
        self.maps_button_box_level_seven_rel_box = BoxLayout(padding=(x * 3, y * 3, x, 0))
        self.maps_button_box_level_seven_rel_coin_box = BoxLayout(padding=(x * 2.2, y, x * 1.4, 0))
        self.next_level_button_level_seven = Button(on_press=self.return_maps, background_color=(255, 255, 0, 0))
        self.maps_button_box_level_seven_rel_box.add_widget(self.next_level_button_level_seven)
        self.maps_button_box_level_seven_rel.add_widget(self.maps_button_box_level_seven_rel_coin_box)
        self.maps_button_box_level_seven_rel.add_widget(self.maps_button_box_level_seven_rel_box)
        self.maps_button_box_rel_letter_boxes_level_seven = AnchorLayout(padding=(x * 1.5, 0, x * 1.4, y * 1.5))
        self.maps_button_box_level_seven_rel.add_widget(self.maps_button_box_rel_letter_boxes_level_seven)
        self.maps_button_box_level_seven.add_widget(self.maps_button_box_level_seven_rel)

        self.maps_button_box_level_eight = BoxLayout(padding=(0, -y * 27, 0, y * 31))
        self.maps_button_box_level_eight_rel = RelativeLayout()
        self.end_level_movie_level_eight = Image(source=('Design Screen/logo.zip'), anim_delay=-1)
        self.maps_button_box_level_eight_rel.add_widget(self.end_level_movie_level_eight)
        self.maps_button_box_level_eight_rel_box = BoxLayout(padding=(x * 3, y * 3, x, 0))
        self.maps_button_box_level_eight_rel_coin_box = BoxLayout(padding=(x * 2.2, y, x * 1.4, 0))
        self.next_level_button_level_eight = Button(on_press=self.return_maps, background_color=(255, 255, 0, 0))
        self.maps_button_box_level_eight_rel_box.add_widget(self.next_level_button_level_eight)
        self.maps_button_box_level_eight_rel.add_widget(self.maps_button_box_level_eight_rel_coin_box)
        self.maps_button_box_level_eight_rel.add_widget(self.maps_button_box_level_eight_rel_box)
        self.maps_button_box_rel_letter_boxes_level_eight = AnchorLayout(padding=(x * 1.5, 0, x * 1.4, y * 1.5))
        self.maps_button_box_level_eight_rel.add_widget(self.maps_button_box_rel_letter_boxes_level_eight)
        self.maps_button_box_level_eight.add_widget(self.maps_button_box_level_eight_rel)

        self.maps_button_box_level_nine = BoxLayout(padding=(0, -y * 27, 0, y * 31))
        self.maps_button_box_level_nine_rel = RelativeLayout()
        self.end_level_movie_level_nine = Image(source=('Design Screen/logo.zip'), anim_delay=-1)
        self.maps_button_box_level_nine_rel.add_widget(self.end_level_movie_level_nine)
        self.maps_button_box_level_nine_rel_box = BoxLayout(padding=(x * 3, y * 3, x, 0))
        self.maps_button_box_level_nine_rel_coin_box = BoxLayout(padding=(x * 2.2, y, x * 1.4, 0))
        self.next_level_button_level_nine = Button(on_press=self.return_maps, background_color=(255, 255, 0, 0))
        self.maps_button_box_level_nine_rel_box.add_widget(self.next_level_button_level_nine)
        self.maps_button_box_level_nine_rel.add_widget(self.maps_button_box_level_nine_rel_coin_box)
        self.maps_button_box_level_nine_rel.add_widget(self.maps_button_box_level_nine_rel_box)
        self.maps_button_box_rel_letter_boxes_level_nine = AnchorLayout(padding=(x * 1.5, 0, x * 1.4, y * 1.5))
        self.maps_button_box_level_nine_rel.add_widget(self.maps_button_box_rel_letter_boxes_level_nine)
        self.maps_button_box_level_nine.add_widget(self.maps_button_box_level_nine_rel)

        self.maps_button_box_level_ten = BoxLayout(padding=(0, -y * 27, 0, y * 31))
        self.maps_button_box_level_ten_rel = RelativeLayout()
        self.end_level_movie_level_ten = Image(source=('Design Screen/logo.zip'), anim_delay=-1)
        self.maps_button_box_level_ten_rel.add_widget(self.end_level_movie_level_ten)
        self.maps_button_box_level_ten_rel_box = BoxLayout(padding=(x * 3, y * 3, x, 0))
        self.maps_button_box_level_ten_rel_coin_box = BoxLayout(padding=(x * 2.2, y, x * 1.4, 0))
        self.next_level_button_level_ten = Button(on_press=self.return_maps, background_color=(255, 255, 0, 0))
        self.maps_button_box_level_ten_rel_box.add_widget(self.next_level_button_level_ten)
        self.maps_button_box_level_ten_rel.add_widget(self.maps_button_box_level_ten_rel_coin_box)
        self.maps_button_box_level_ten_rel.add_widget(self.maps_button_box_level_ten_rel_box)
        self.maps_button_box_rel_letter_boxes_level_ten = AnchorLayout(padding=(x * 1.5, 0, x * 1.4, y * 1.5))
        self.maps_button_box_level_ten_rel.add_widget(self.maps_button_box_rel_letter_boxes_level_ten)
        self.maps_button_box_level_ten.add_widget(self.maps_button_box_level_ten_rel)


        self.one_stars = Image(source=('Design Screen/one_star.zip'), allow_stretch=True,
                               keep_ratio=False, anim_delay=-1, anim_loop=1)
        self.two_stars = Image(source=('Design Screen/two_star.zip'), allow_stretch=True,
                               keep_ratio=False, anim_delay=-1, anim_loop=1)
        self.three_stars = Image(source=('Design Screen/three_star.zip'), allow_stretch=True,
                               keep_ratio=False, anim_delay=-1, anim_loop=1)

        self.maps_image_screen = Screen(name='Map')
        self.scroll_screen = ScrollView(size=(Window.width, Window.height), size_hint=(1, None),  do_scroll_x = False, scroll_y = 0, bar_color = [0,0,0,0])
        self.maps_image_rel = RelativeLayout(size = (Window.width, y*71.5), size_hint_y=None)


        self.maps_image_level_one = Image(source=('Design Screen/select_level_screen.png'))
        self.maps_image_shadow_box_level_one = BoxLayout(padding = (0, 0, 0, y * 4))
        self.maps_image_shadow_box_level_one.add_widget(Button(background_color = (0,0,0, .5)))
        self.button_level_one = Button(background_color = (0,0,0,0), on_press = self.start_level)
        self.stars_box_level_one = BoxLayout(padding = (x*2, y*69.5, x*2, y*1.2))
        self.button_box_level_one = BoxLayout(padding = (0, y * 67.5, 0, y * 2))
        self.button_box_level_one.add_widget(self.button_level_one)

        self.maps_image_level_two = Image(source=('Design Screen/select_level_screen.png'))
        self.maps_image_shadow_box_level_two = BoxLayout(padding=(0, 0, 0, y * 5.9))
        self.maps_image_shadow_box_level_two.add_widget(Button(background_color = (0,0,0, .5)))
        self.button_level_two = Button(background_color=(0, 0, 0, .0), on_press=self.start_level)
        self.stars_box_level_two = BoxLayout(padding = (x*2, y*67.5, x*2, y*3.2))
        self.button_box_level_two = BoxLayout(padding=(0, y * 65.5, 0, y * 3.9))
        self.button_box_level_two.add_widget(self.button_level_two)

        self.maps_image_level_three = Image(source=('Design Screen/select_level_screen.png'))
        self.maps_image_shadow_box_level_three = BoxLayout(padding=(0, 0, 0, y * 7.9))
        self.maps_image_shadow_box_level_three.add_widget(Button(background_color = (0,0,0, .5)))
        self.button_level_three = Button(background_color=(0, 0, 0, 0), on_press=self.start_level)
        self.stars_box_level_three = BoxLayout(padding = (x*2, y*65.5, x*2, y*5.2))
        self.button_box_level_three = BoxLayout(padding=(0, y * 63.5, 0, y * 5.9))
        self.button_box_level_three.add_widget(self.button_level_three)

        self.maps_image_level_four = Image(source=('Design Screen/select_level_screen.png'))
        self.maps_image_shadow_box_level_four = BoxLayout(padding=(0, 0, 0, y * 9.9))
        self.maps_image_shadow_box_level_four.add_widget(Button(background_color = (0,0,0, .5)))
        self.button_level_four = Button(background_color=(0, 0, 0, 0), on_press=self.start_level)
        self.stars_box_level_four = BoxLayout(padding = (x*2, y*63.5, x*2, y*7.2))
        self.button_box_level_four = BoxLayout(padding=(0, y * 61.5, 0, y * 7.9))
        self.button_box_level_four.add_widget(self.button_level_four)

        self.maps_image_level_five = Image(source=('Design Screen/select_level_screen.png'))
        self.maps_image_shadow_box_level_five = BoxLayout(padding=(0, 0, 0, y * 11.9))
        self.maps_image_shadow_box_level_five.add_widget(Button(background_color = (0,0,0, .5)))
        self.button_level_five = Button(background_color=(0, 0, 0, 0), on_press=self.start_level)
        self.stars_box_level_five = BoxLayout(padding = (x*2, y*61.5, x*2, y*9.2))
        self.button_box_level_five = BoxLayout(padding=(0, y * 59.5, 0, y * 9.9))
        self.button_box_level_five.add_widget(self.button_level_five)

        self.maps_image_level_six = Image(source=('Design Screen/select_level_screen.png'))
        self.maps_image_shadow_box_level_six = BoxLayout(padding=(0, 0, 0, y * 13.9))
        self.maps_image_shadow_box_level_six.add_widget(Button(background_color = (0,0,0, .5)))
        self.button_level_six = Button(background_color=(0, 0, 0, 0), on_press=self.start_level)
        self.stars_box_level_six = BoxLayout(padding = (x*2, y*59.5, x*2, y*11.2))
        self.button_box_level_six = BoxLayout(padding=(0, y * 57.5, 0, y * 11.9))
        self.button_box_level_six.add_widget(self.button_level_six)

        self.maps_image_level_seven = Image(source=('Design Screen/select_level_screen.png'))
        self.maps_image_shadow_box_level_seven = BoxLayout(padding=(0, 0, 0, y * 15.9))
        self.maps_image_shadow_box_level_seven.add_widget(Button(background_color=(0, 0, 0, .5)))
        self.button_level_seven = Button(background_color=(0, 0, 0, 0), on_press=self.start_level)
        self.stars_box_level_seven = BoxLayout(padding=(x * 2, y * 57.5, x * 2, y * 13.2))
        self.button_box_level_seven = BoxLayout(padding=(0, y * 55.5, 0, y * 13.9))
        self.button_box_level_seven.add_widget(self.button_level_seven)

        self.maps_image_level_eight = Image(source=('Design Screen/select_level_screen.png'))
        self.maps_image_shadow_box_level_eight = BoxLayout(padding=(0, 0, 0, y * 17.9))
        self.maps_image_shadow_box_level_eight.add_widget(Button(background_color=(0, 0, 0, .5)))
        self.button_level_eight = Button(background_color=(0, 0, 0, 0), on_press=self.start_level)
        self.stars_box_level_eight = BoxLayout(padding=(x * 2, y * 55.5, x * 2, y * 15.2))
        self.button_box_level_eight = BoxLayout(padding=(0, y * 53.5, 0, y * 15.9))
        self.button_box_level_eight.add_widget(self.button_level_eight)

        self.maps_image_level_nine = Image(source=('Design Screen/select_level_screen.png'))
        self.maps_image_shadow_box_level_nine = BoxLayout(padding=(0, 0, 0, y * 19.9))
        self.maps_image_shadow_box_level_nine.add_widget(Button(background_color=(0, 0, 0, .5)))
        self.button_level_nine = Button(background_color=(0, 0, 0, 0), on_press=self.start_level)
        self.stars_box_level_nine = BoxLayout(padding=(x * 2, y * 53.5, x * 2, y * 17.2))
        self.button_box_level_nine = BoxLayout(padding=(0, y * 51.5, 0, y * 17.9))
        self.button_box_level_nine.add_widget(self.button_level_nine)

        self.maps_image_level_ten = Image(source=('Design Screen/select_level_screen.png'))
        self.maps_image_shadow_box_level_ten = BoxLayout(padding=(0, 0, 0, y * 21.9))
        self.maps_image_shadow_box_level_ten.add_widget(Button(background_color=(0, 0, 0, .5)))
        self.button_level_ten = Button(background_color=(0, 0, 0, 0), on_press=self.start_level)
        self.stars_box_level_ten = BoxLayout(padding=(x * 2, y * 51.5, x * 2, y * 19.2))
        self.button_box_level_ten = BoxLayout(padding=(0, y * 49.5, 0, y * 19.9))
        self.button_box_level_ten.add_widget(self.button_level_ten)




        self.maps_image_screen.add_widget(self.scroll_screen)


        self.next_floor_button_box =  RelativeLayout()


        # флаги нанесение повреждений
        self.one_hit = False

        # флаг с началом фазы полета
        self.start_left = False
        self.start_right = False

        #начало фазы приседания
        self.start_sit = False

        # флаг с прохождением уровня
        self.first_level_complete = False
        self.second_level_complete = False
        self.three_level_complete = False
        self.four_level_complete = False
        self.five_level_complete = False
        self.six_level_complete = False
        self.seven_level_complete = False
        self.eight_level_complete = False
        self.nine_level_complete = False
        self.ten_level_complete = False

        #флаг с началом уровня
        self.first_level_start = False
        self.second_level_start = False
        self.three_level_start = False
        self.four_level_start = False
        self.five_level_start = False
        self.six_level_start = False
        self.seven_level_start = False
        self.eight_level_start = False
        self.nine_level_start = False
        self.ten_level_start = False

        self.down_number = 0
        self.static_number = 0

        self.start_box = BoxLayout(padding=(x, y * 3, x, y * 3))
        self.start_box_rel = RelativeLayout(size=(x * 4, y * 2))
        self.start_box_rel.add_widget(
            Image(source=('Design Screen/play_but.zip'), anim_delay=.02, allow_stretch=False, keep_ratio=False))
        self.start_box_rel.add_widget(Button(on_press=(self.start), background_color=(0, 0, 0, 0)))
        self.start_box.add_widget(self.start_box_rel)


        """_________________________________________________________________________________________________________"""
        # ..............................................................................добавляем экран с первым уровнем
        self.first_level = Screen(name=('First_level'))
        self.first_level_screen = RelativeLayout()
        self.first_level_screen_child = RelativeLayout()

        self.climb_screen_level_one = RelativeLayout()
        self.sky_box_level_one = BoxLayout(padding=(-x*10, -y*12, -x*10, 0))
        self.sky_image_level_one = Image(source=('Design Screen/небо.png'), allow_stretch=True,
                                keep_ratio=False)
        self.sky_box_level_one.add_widget(self.sky_image_level_one)
        self.wall_box_level_one = BoxLayout(padding = (0, -y*24, 0, 0))
        self.climb_wall_level_one = Image(source=('Design Screen/фон_стена_дерево_3.png'), allow_stretch = True,
                                                    keep_ratio = False
                                                    )
        self.wall_box_level_one.add_widget(self.climb_wall_level_one)
        self.green_box_level_one = BoxLayout(padding = (0, -y*12, 0, 0))
        self.green_image_level_one = Image(source=('Design Screen/трава_фон.png'), allow_stretch = True,
                                                    keep_ratio = False)
        self.green_box_level_one.add_widget(self.green_image_level_one)
        self.frages_box_level_one =  BoxLayout(padding=(x*3, -y, x * 2.5, y * 8.6))
        self.frages_box_image_level_one = BoxLayout(padding=(x*2.8, -y*1.7, x * 1.4, y *8.4))
        self.frages_box_image_level_one.add_widget(Image(source=('Design Screen/disk.zip'), anim_delay = .02, allow_stretch=True, keep_ratio=False))
        self.frag_level_one = Widget()
        self.frages_box_1_level_one = AnchorLayout(
            anchor_x='left', anchor_y='bottom', padding=(x*3, -y * 6.8, x * 2.5, y * 15.0))
        self.frages_box_image_1_level_one = AnchorLayout(
            anchor_x='left', anchor_y='bottom', padding=(x*2.8, -y*7.7, x * 1.4, y *14.4))
        self.frages_box_image_1_level_one.add_widget(
            Image(source=('Design Screen/disk.zip'), anim_delay = .02, allow_stretch=True, keep_ratio=False))
        self.frag_1_level_one = Widget()
        self.frages_box_2_level_one = AnchorLayout(
            anchor_x='left', anchor_y='bottom', padding=(x_level*2, -y_level*19.5, x_level, y_level *31))
        self.frages_box_image_2_level_one = AnchorLayout(
            anchor_x='left', anchor_y='bottom', padding=(x*2.8, -y_level*20.5, x * 1.4, y_level*30))
        self.frages_box_image_2_level_one.add_widget(
            Image(source=('Design Screen/disk.zip'),anim_delay = .02, allow_stretch=True, keep_ratio=False))
        self.frag_2_level_one = Widget()
        self.frages_box_level_one.add_widget(self.frag_level_one)
        self.frages_box_1_level_one.add_widget(self.frag_1_level_one)
        self.frages_box_2_level_one.add_widget(self.frag_2_level_one)


        self.coin_box_1_level_one = AnchorLayout(padding=(x_level*1.5, 0, x_level * 2, y*7))
        self.coin_box_2_level_one = AnchorLayout(padding=(x_level * 0.5, -y, x_level * 3, y * 8))
        self.coin_box_3_level_one = AnchorLayout(padding=(x_level * 0.5, -y * 2, x_level * 3, y * 9))
        self.coin_box_4_level_one = AnchorLayout(padding=(x_level * 1.5, -y *3, x_level * 2, y * 10))
        self.coin_box_5_level_one = AnchorLayout(padding=(x_level * 1.5, -y * 5, x_level * 2, y * 12))
        self.coin_box_6_level_one = AnchorLayout(padding=(x_level * 1.5, -y * 6, x_level * 2, y * 13))
        self.coin_box_7_level_one= AnchorLayout(padding=(x_level * 0.5, -y * 7, x_level * 3, y * 14))
        self.coin_box_8_level_one = AnchorLayout(padding=(x_level * 0.5, -y * 8, x_level * 3, y * 15))
        self.coin_box_9_level_one = AnchorLayout(padding=(x_level * 1.5, -y * 10, x_level * 2, y * 17))
        self.coin_box_11_level_one = AnchorLayout(padding=(x_level * 1.5, -y * 13, x_level * 2, y * 20))
        self.coin_box_12_level_one = AnchorLayout(padding=(x_level * 0.5, -y * 14, x_level * 3, y * 21))
        self.coin_box_13_level_one = AnchorLayout(padding=(x_level * 0.5, -y * 15, x_level * 3, y * 22))
        self.coin_box_14_level_one = AnchorLayout(padding=(x_level * 1.5, -y * 16, x_level * 2, y * 23))

        self.coin_boxes_level_one = [self.coin_box_1_level_one, self.coin_box_2_level_one, self.coin_box_3_level_one, self.coin_box_4_level_one, self.coin_box_5_level_one,
                           self.coin_box_6_level_one, self.coin_box_7_level_one, self.coin_box_8_level_one, self.coin_box_9_level_one,
                           self.coin_box_11_level_one, self.coin_box_12_level_one, self.coin_box_13_level_one, self.coin_box_14_level_one ]

        self.coins_level_one = []
        self.coin_check_level_one = 0

        for i in range(13):
            i = Coin()
            self.coins_level_one.append(i)

        for a in self.coin_boxes_level_one[:]:
            a.add_widget(self.coins_level_one[self.coin_check_level_one])
            self.coin_check_level_one += 1

        self.coin_count_level_one = 0
        self.knight_image_box_level_one = BoxLayout(padding=(-x,0,x/1.5,0))
        self.knight_image_jump_level_one = Widget()
        self.knight_image_end_level_one = Widget()
        self.knight_image_start_level_one = Image(source=('Design Screen/a.png'))
        self.knight_image_walk_level_one = Widget()
        self.knight_image_sit_level_one = Widget()
        self.knight_image_sit_up_level_one = Widget()
        self.knight_box_level_one = BoxLayout(padding=(x*2.2, y*4, x*2.8, y*3))
        self.knight_box_button_level_one = Widget()

        self.word_box_level_one = BoxLayout(padding=(x_level*0.7, -y * 11, x_level * 2.8, y * 18))
        self.word_image_level_one = Image(source = ('Design Screen/буквы/буква К.png'))
        self.word_box_level_one.add_widget(self.word_image_level_one)
        self.Knight_box_letter_level_one = BoxLayout(padding=(x_level * 0.2, y*0.6, x_level * 2, y * 7))
        self.Knight_image_box_letter_level_one = Image(source=('Design Screen/буквы/KNIGHT_1_level.png'))
        self.Knight_box_letter_level_one.add_widget(self.Knight_image_box_letter_level_one)
        self.Knight_box_letter_level_one_empty = BoxLayout(padding=(x_level * 0.2, y * 0.6, x_level * 2, y * 7))

        self.knight_box_level_one.add_widget(self.knight_box_button_level_one)

        self.knight_image_box_level_one.add_widget(self.knight_image_start_level_one)
        self.knight_level_complete_box = BoxLayout(padding=(0, -y * 28.5, 0, y * 27.9))
        self.knight_level_complete_box.add_widget(
            Image(source=('Design Screen/end_level_animation_4.zip'), anim_delay=.04, allow_stretch=True,
                  keep_ratio=False))
        self.climb_screen_level_one.add_widget(self.knight_level_complete_box)
        self.climb_screen_level_one.add_widget(self.wall_box_level_one)
        self.climb_screen_level_one.add_widget(self.green_box_level_one)
        self.climb_screen_level_one.add_widget(self.frages_box_level_one)
        self.climb_screen_level_one.add_widget(self.frages_box_image_level_one)
        self.climb_screen_level_one.add_widget(self.knight_box_level_one)
        self.climb_screen_level_one.add_widget(self.knight_image_box_level_one)
        self.climb_screen_level_one.add_widget(self.frages_box_1_level_one)
        self.climb_screen_level_one.add_widget(self.frages_box_image_1_level_one)
        self.climb_screen_level_one.add_widget(self.frages_box_2_level_one)
        self.climb_screen_level_one.add_widget(self.frages_box_image_2_level_one)
        self.climb_screen_level_one.add_widget(self.word_box_level_one)


        for i in self.coin_boxes_level_one[:]:
            self.climb_screen_level_one.add_widget(i)
        self.screen_box_touch = BoxLayout()
        self.first_level_screen_child.add_widget(self.sky_box_level_one)
        self.first_level_screen_child.add_widget(self.climb_screen_level_one)

        self.first_level_screen.add_widget(self.first_level_screen_child)

        item_coin_box_level_one = BoxLayout(padding=(x * 4, y / 5, x, y * 7))
        item_coin_box_level_one.add_widget(Image(source=('Design Screen/монетка.zip'), anim_delay=.1,allow_stretch=False,keep_ratio=False))
        self.coin_image_count = Label(text=str(self.coin_collect), font_size='60sp',
                                                color=[0, 0, 0, 1], bold=24)

        self.swipe_level_one = Slider(min=-1, max=1, value=0, step = .5,background_width=(0), cursor_size = (0,0),
                        on_touch_up = self.on_touch_up, on_touch_move = self.on_touch_move, on_touch_down = self.on_touch_down)

        self.first_level.add_widget(self.first_level_screen)

        """_________________________________________________________________________________________________________"""
        # ......................................................................................добавляем второй уровень
        self.second_level = Screen(name=('Second_level'))
        self.second_level_screen = RelativeLayout()
        self.second_level_screen_child = RelativeLayout()

        self.climb_screen_level_two = RelativeLayout()
        self.sky_box_level_two = BoxLayout(padding=(-x*10, -y*10, -x*10, -y*2))
        self.sky_image_level_two = Image(source=('Design Screen/небо.png'), allow_stretch=True,
                               keep_ratio=False)
        self.sky_box_level_two.add_widget(self.sky_image_level_two)

        self.wall_box_level_two = BoxLayout(padding=(0, -y * 24, 0, 0))
        self.climb_wall_level_two = Image(source=('Design Screen/фон_стена_дерево_3.png'), allow_stretch=True,
                                keep_ratio=False)

        self.wall_box_level_two.add_widget(self.climb_wall_level_two)



        self.coin_box_level_two_1 = AnchorLayout(padding=(x_level * 1.5, 0, x_level * 2, y * 7))
        self.coin_box_level_two_2 = AnchorLayout(padding=(x_level * 0.5, -y, x_level * 3, y * 8))
        self.coin_box_level_two_3 = AnchorLayout(padding=(x_level * 1.5, -y *2, x_level * 2, y * 9))
        self.coin_box_level_two_4 = AnchorLayout(padding=(x_level * 1.5, -y * 5, x_level * 2, y * 12))
        self.coin_box_level_two_5 = AnchorLayout(padding=(x_level * 0.5, -y * 6, x_level * 3, y * 13))
        self.coin_box_level_two_6 = AnchorLayout(padding=(x_level * 1.5, -y * 7, x_level * 2, y * 14))
        self.coin_box_level_two_7 = AnchorLayout(padding=(x_level * 1.5, -y * 10, x_level * 2, y * 17))
        self.coin_box_level_two_8 = AnchorLayout(padding=(x_level * 0.5, -y * 11, x_level * 3, y * 18))
        self.coin_box_level_two_9 = AnchorLayout(padding=(x_level * 1.5, -y * 12, x_level * 2, y * 19))


        self.coin_boxes_level_two = [self.coin_box_level_two_1, self.coin_box_level_two_2, self.coin_box_level_two_3,
                                     self.coin_box_level_two_4, self.coin_box_level_two_5, self.coin_box_level_two_6,
                                     self.coin_box_level_two_7, self.coin_box_level_two_8, self.coin_box_level_two_9]

        self.coins_level_two = []
        self.coin_check_level_two = 0

        for i in range(9):
            i = Coin()
            self.coins_level_two.append(i)
        for a in self.coin_boxes_level_two[:]:
            a.add_widget(self.coins_level_two[self.coin_check_level_two])
            self.coin_check_level_two += 1


        self.coin_count_level_two = 0

        self.knight_image_box_level_two = BoxLayout(padding=(-x,0,x/1.5,0))
        self.knight_image_jump_level_two = Widget()
        self.knight_image_end_level_two = Widget()
        self.knight_image_start_level_two = Image(source=('Design Screen/a.png'))
        self.knight_image_walk_level_two = Widget()
        self.knight_image_sit_level_two = Widget()
        self.knight_image_sit_up_level_two = Widget()

        self.frages_box_level_two_down = BoxLayout(padding=(x * 2, 0, x * 3.5, y*6))
        self.frages_box_image_level_two_down = BoxLayout(padding=(x * 2, 0, x * 3.5, y*6))
        self.frages_box_image_level_two_down.add_widget(
            Image(source=('Design Screen/стрела.zip'), anim_delay=.1, keep_ratio=False,allow_stretch=True))
        self.frag_level_two_down = Widget()

        self.frages_box_1_level_two_down = AnchorLayout(
            anchor_x='left', anchor_y='bottom', padding=(x * 2, 0, x * 3.5, y*6))
        self.frages_box_image_1_level_two_down = AnchorLayout(
            anchor_x='left', anchor_y='bottom', padding=(x * 2, 0, x * 3.5, y*6))
        self.frages_box_image_1_level_two_down.add_widget(
            Image(source=('Design Screen/стрела.zip'), anim_delay=.2, allow_stretch=True, keep_ratio=False))
        self.frag_1_level_two_down = Widget()

        self.frages_box_2_level_two_down = AnchorLayout(
            anchor_x='left', anchor_y='bottom', padding=(x * 2, 0, x * 3.5, y*6))
        self.frages_box_image_2_level_two_down = AnchorLayout(
            anchor_x='left', anchor_y='bottom', padding=(x * 2, 0, x * 3.5, y*6))
        self.frages_box_image_2_level_two_down.add_widget(
            Image(source=('Design Screen/стрела.zip'), anim_delay=.08, allow_stretch=True, keep_ratio=False))
        self.frag_2_level_two_down = Widget()

        self.frages_box_level_two_down.add_widget(self.frag_level_two_down)
        self.frages_box_1_level_two_down.add_widget(self.frag_1_level_two_down)
        self.frages_box_2_level_two_down.add_widget(self.frag_2_level_two_down)

        self.knight_box_level_two = BoxLayout(padding=(x * 2.2, y * 4, x * 2.8, y * 3))
        self.frages_box_image_level_two_down.y = self.knight_box_level_two.y + y*28
        self.frages_box_level_two_down.y = self.knight_box_level_two.y + y*28
        self.frages_box_image_1_level_two_down.y = self.knight_box_level_two.y + y*28
        self.frages_box_1_level_two_down.y = self.knight_box_level_two.y + y*28
        self.frages_box_image_2_level_two_down.y = self.knight_box_level_two.y + y*28
        self.frages_box_2_level_two_down.y = self.knight_box_level_two.y + y*28
        self.knight_box_button_level_two = Widget()

        self.word_box_level_two = BoxLayout(padding=(x_level * 1.5, -y * 14, x_level * 2, y * 21))
        self.word_image_level_two = Image(source=('Design Screen/буквы/буква N.png'))
        self.word_box_level_two.add_widget(self.word_image_level_two)
        self.Knight_box_letter_level_two = BoxLayout(padding=(x_level * 0.2, y * 0.6, x_level * 2, y * 7))
        self.Knight_image_box_letter_level_two = Image(source=('Design Screen/буквы/KNIGHT_2_level.png'))
        self.Knight_box_letter_level_two.add_widget(self.Knight_image_box_letter_level_two)
        self.Knight_box_letter_level_two_empty = BoxLayout(padding=(x_level * 0.2, y * 0.6, x_level * 2, y * 7))

        self.knight_box_level_two.add_widget(self.knight_box_button_level_two)
        self.knight_image_box_level_two.add_widget(self.knight_image_start_level_two)
        self.knight_level_two_complete_box = BoxLayout(padding=(0, -y * 28, 0, y * 28))
        self.knight_level_two_complete_box.add_widget(
            Image(source=('Design Screen/end_level_animation_2.zip'), anim_delay=.04, allow_stretch=True,
                  keep_ratio=False))
        self.climb_screen_level_two.add_widget(self.knight_level_two_complete_box)
        self.climb_screen_level_two.add_widget(self.wall_box_level_two)
        self.climb_screen_level_two.add_widget(self.frages_box_level_two_down)
        self.climb_screen_level_two.add_widget(self.frages_box_image_level_two_down)
        self.climb_screen_level_two.add_widget(self.frages_box_1_level_two_down)
        self.climb_screen_level_two.add_widget(self.frages_box_image_1_level_two_down)
        self.climb_screen_level_two.add_widget(self.frages_box_2_level_two_down)
        self.climb_screen_level_two.add_widget(self.frages_box_image_2_level_two_down)
        self.climb_screen_level_two.add_widget(self.knight_box_level_two)
        self.climb_screen_level_two.add_widget(self.knight_image_box_level_two)
        self.climb_screen_level_two.add_widget(self.word_box_level_two)
        for i in self.coin_boxes_level_two[:]:
            self.climb_screen_level_two.add_widget(i)
        self.second_level_screen_child.add_widget(self.sky_box_level_two)
        self.second_level_screen_child.add_widget(self.climb_screen_level_two)
        self.second_level_screen.add_widget(self.second_level_screen_child)

        self.swipe_level_two = Slider(min=-1, max=1, value=0, step=.5, background_width=(0), cursor_size=(0, 0),
                                      on_touch_up=self.on_touch_up, on_touch_move=self.on_touch_move,
                                      on_touch_down=self.on_touch_down)

        self.second_level.add_widget(self.second_level_screen)

        """_________________________________________________________________________________________________________"""
        # ......................................................................................добавляем третий уровень
        self.three_level = Screen(name=('Three_level'))
        self.three_level_screen = RelativeLayout()
        self.three_level_screen_child = RelativeLayout()
        self.climb_screen_level_three = RelativeLayout()
        self.sky_box_level_three = BoxLayout(padding=(-x*10, -y*8, -x*10, -y*4))
        self.sky_image_level_three = Image(source=('Design Screen/небо.png'), allow_stretch=True,
                                         keep_ratio=False)
        self.sky_box_level_three.add_widget(self.sky_image_level_three)

        self.wall_box_level_three = BoxLayout(padding=(0, -y * 24, 0, 0))
        self.climb_wall_level_three = Image(source=('Design Screen/фон_стена_дерево_3.png'), allow_stretch=True,
                                          keep_ratio=False)

        self.wall_box_level_three.add_widget(self.climb_wall_level_three)



        self.coin_box_level_three_1 = AnchorLayout(padding=(x_level * 1.5, 0, x_level * 2, y * 7))
        self.coin_box_level_three_2 = AnchorLayout(padding=(x_level * 1.5, -y, x_level * 2, y * 8))
        self.coin_box_level_three_3 = AnchorLayout(padding=(x_level * 1.5, -y * 2, x_level * 2, y * 9))
        self.coin_box_level_three_4 = AnchorLayout(padding=(x_level * 1.5, -y * 5, x_level * 2, y * 12))
        self.coin_box_level_three_5 = AnchorLayout(padding=(x_level * 0.5, -y * 6, x_level * 3, y * 13))
        self.coin_box_level_three_6 = AnchorLayout(padding=(x_level * 1.5, -y * 7, x_level * 2, y * 14))
        self.coin_box_level_three_7 = AnchorLayout(padding=(x_level * 1.5, -y * 10, x_level * 2, y * 17))
        self.coin_box_level_three_8 = AnchorLayout(padding=(x_level * 0.5, -y * 11, x_level * 3, y * 18))
        self.coin_box_level_three_9 = AnchorLayout(padding=(x_level * 1.5, -y * 12, x_level * 2, y * 19))
        self.coin_box_level_three_10 = AnchorLayout(padding=(x_level * 1.5, -y * 14, x_level * 2, y * 21))
        self.coin_box_level_three_11 = AnchorLayout(padding=(x_level * 0.5, -y * 15, x_level * 3, y * 22))
        self.coin_box_level_three_12 = AnchorLayout(padding=(x_level * 1.5, -y * 16, x_level * 2, y * 23))

        self.coin_boxes_level_three = [self.coin_box_level_three_1, self.coin_box_level_three_2, self.coin_box_level_three_3,
                                     self.coin_box_level_three_4, self.coin_box_level_three_5, self.coin_box_level_three_6,
                                     self.coin_box_level_three_7, self.coin_box_level_three_8, self.coin_box_level_three_9,
                                       self.coin_box_level_three_10, self.coin_box_level_three_11, self.coin_box_level_three_12]

        self.coins_level_three = []

        self.coin_check_level_three = 0

        for i in range(12):
            i = Coin()
            self.coins_level_three.append(i)

        for a in self.coin_boxes_level_three[:]:
            a.add_widget(self.coins_level_three[self.coin_check_level_three])
            self.coin_check_level_three += 1

        self.coin_count_level_three = 0

        self.knight_image_box_level_three = BoxLayout(padding=(-x,0,x/1.5,0))
        self.knight_image_jump_level_three = Widget()
        self.knight_image_end_level_three = Widget()
        self.knight_image_start_level_three = Image(source=('Design Screen/a.png'))
        self.knight_image_walk_level_three = Widget()
        self.knight_image_sit_level_three = Widget()
        self.knight_image_sit_up_level_three = Widget()
        self.knight_box_level_three = BoxLayout(padding=(x * 2.2, y * 4, x * 2.8, y * 3))
        self.frages_box_level_three = BoxLayout(padding=(x*3, -y*5, x * 2.5, y * 13.6))
        self.frages_box_image_level_three = BoxLayout(padding=(x*2.8, -y*6.1, x * 1.4, y *12.8))
        self.frages_box_image_level_three.add_widget(
            Image(source=('Design Screen/disk.zip'), anim_delay=.01, keep_ratio=False, allow_stretch=True))
        self.frag_level_three = Widget()

        self.frages_box_1_level_three = BoxLayout(padding=(x * 3, -y * 10, x * 2.5, y * 18.6))
        self.frages_box_image_1_level_three = BoxLayout(padding=(x * 2.8, -y * 11.1, x * 1.4, y * 17.8))
        self.frages_box_image_1_level_three.add_widget(
            Image(source=('Design Screen/disk.zip'), anim_delay=.01, keep_ratio=False, allow_stretch=True))
        self.frag_1_level_three = Widget()

        self.frages_box_level_three_down = BoxLayout(padding=(x * 2, 0, x * 3.5, y * 6))
        self.frages_box_image_level_three_down = BoxLayout(padding=(x * 2, 0, x * 3.5, y * 6))
        self.frages_box_image_level_three_down.add_widget(Image(source=('Design Screen/стрела.zip'), anim_delay=.1, keep_ratio=False, allow_stretch=True))
        self.frag_level_three_down = Widget()
        self.frages_box_image_level_three_down.y = self.knight_box_level_three.y + y * 48
        self.frages_box_level_three_down.y = self.knight_box_level_three.y + y * 48

        self.frages_box_level_three_down.add_widget(self.frag_level_three_down)
        self.frages_box_level_three.add_widget(self.frag_level_three)
        self.frages_box_1_level_three.add_widget(self.frag_1_level_three)

        self.word_box_level_three = BoxLayout(padding=(x_level * 0.7, -y * 12, x_level * 2.8, y * 19))
        self.word_image_level_three = Image(source=('Design Screen/буквы/буква I.png'))
        self.word_box_level_three.add_widget(self.word_image_level_three)
        self.Knight_box_letter_level_three = BoxLayout(padding=(x_level * 0.2, y * 0.6, x_level * 2, y * 7))
        self.Knight_image_box_letter_level_three = Image(source=('Design Screen/буквы/KNIGHT_3_level.png'))
        self.Knight_box_letter_level_three.add_widget(self.Knight_image_box_letter_level_three)
        self.Knight_box_letter_level_three_empty = BoxLayout(padding=(x_level * 0.2, y * 0.6, x_level * 2, y * 7))

        self.knight_box_button_level_three = Widget()
        self.knight_box_level_three.add_widget(self.knight_box_button_level_three)
        self.knight_image_box_level_three.add_widget(self.knight_image_start_level_three)
        self.knight_level_three_complete_box = BoxLayout(padding=(0, -y * 28.5, 0, y * 27.9))
        self.knight_level_three_complete_box.add_widget(
            Image(source=('Design Screen/end_level_animation_3.zip'), anim_delay=.018, allow_stretch=True,
                  keep_ratio=False))
        self.climb_screen_level_three.add_widget(self.knight_level_three_complete_box)
        self.climb_screen_level_three.add_widget(self.wall_box_level_three)
        self.climb_screen_level_three.add_widget(self.frages_box_level_three_down)
        self.climb_screen_level_three.add_widget(self.frages_box_image_level_three_down)
        self.climb_screen_level_three.add_widget(self.frages_box_level_three)
        self.climb_screen_level_three.add_widget(self.frages_box_1_level_three)
        self.climb_screen_level_three.add_widget(self.frages_box_image_level_three)
        self.climb_screen_level_three.add_widget(self.frages_box_image_1_level_three)
        self.climb_screen_level_three.add_widget(self.knight_box_level_three)
        self.climb_screen_level_three.add_widget(self.knight_image_box_level_three)
        self.climb_screen_level_three.add_widget(self.word_box_level_three)
        for i in self.coin_boxes_level_three[:]:
            self.climb_screen_level_three.add_widget(i)
        self.three_level_screen_child.add_widget(self.sky_box_level_three)
        self.three_level_screen_child.add_widget(self.climb_screen_level_three)
        self.three_level_screen.add_widget(self.three_level_screen_child)

        self.swipe_level_three = Slider(min=-1, max=1, value=0, step=.5, background_width=(0), cursor_size=(0, 0),
                                      on_touch_up=self.on_touch_up, on_touch_move=self.on_touch_move,
                                      on_touch_down=self.on_touch_down)
        self.three_level.add_widget(self.three_level_screen)

        "_____________________________________________________________________________________________________________"

        # ......................................................................................добавляем четвертый уровень
        self.four_level = Screen(name=('Four_level'))
        self.four_level_screen = RelativeLayout()
        self.four_level_screen_child = RelativeLayout()
        self.climb_screen_level_four = RelativeLayout()
        self.sky_box_level_four = BoxLayout(padding=(-x*10, -y*6, -x*10, -y*6))
        self.sky_image_level_four = Image(source=('Design Screen/небо.png'), allow_stretch=True,
                                           keep_ratio=False)
        self.sky_box_level_four.add_widget(self.sky_image_level_four)

        self.wall_box_level_four = BoxLayout(padding=(0, -y * 24, 0, 0))
        self.climb_wall_level_four = Image(source=('Design Screen/фон_стена_дерево_3.png'), allow_stretch=True,
                                            keep_ratio=False)

        self.wall_box_level_four.add_widget(self.climb_wall_level_four)
        self.coin_box_level_four_1 = AnchorLayout(padding=(x_level * 1.5, 0, x_level * 2, y * 7))
        self.coin_box_level_four_2 = AnchorLayout(padding=(x_level * 1.5, -y, x_level * 2, y * 8))
        self.coin_box_level_four_3 = AnchorLayout(padding=(x_level * 1.5, -y * 2, x_level * 2, y * 9))
        self.coin_box_level_four_4 = AnchorLayout(padding=(x_level * 1.5, -y * 5, x_level * 2, y * 12))
        self.coin_box_level_four_5 = AnchorLayout(padding=(x_level * 0.5, -y * 6, x_level * 3, y * 13))
        self.coin_box_level_four_6 = AnchorLayout(padding=(x_level * 1.5, -y * 7, x_level * 2, y * 14))
        self.coin_box_level_four_7 = AnchorLayout(padding=(x_level * 1.5, -y * 10, x_level * 2, y * 17))
        self.coin_box_level_four_8 = AnchorLayout(padding=(x_level * 0.5, -y * 11, x_level * 3, y * 18))
        self.coin_box_level_four_9 = AnchorLayout(padding=(x_level * 1.5, -y * 12, x_level * 2, y * 19))
        self.coin_box_level_four_10 = AnchorLayout(padding=(x_level * 1.5, -y * 14, x_level * 2, y * 21))
        self.coin_box_level_four_11 = AnchorLayout(padding=(x_level * 0.5, -y * 15, x_level * 3, y * 22))
        self.coin_box_level_four_12 = AnchorLayout(padding=(x_level * 1.5, -y * 16, x_level * 2, y * 23))

        self.coin_boxes_level_four = [self.coin_box_level_four_1, self.coin_box_level_four_2,
                                       self.coin_box_level_four_3,
                                       self.coin_box_level_four_4, self.coin_box_level_four_5,
                                       self.coin_box_level_four_6,
                                       self.coin_box_level_four_7, self.coin_box_level_four_8,
                                       self.coin_box_level_four_9,
                                       self.coin_box_level_four_10, self.coin_box_level_four_11,
                                       self.coin_box_level_four_12]

        self.coins_level_four = []

        self.coin_check_level_four = 0

        for i in range(12):
            i = Coin()
            self.coins_level_four.append(i)

        for a in self.coin_boxes_level_four[:]:
            a.add_widget(self.coins_level_four[self.coin_check_level_four])
            self.coin_check_level_four += 1

        self.coin_count_level_four = 0

        self.knight_image_box_level_four = BoxLayout(padding=(-x,0,x/1.5,0))

        self.knight_image_jump_level_four = Widget()
        self.knight_image_end_level_four = Widget()
        self.knight_image_start_level_four = Image(source=('Design Screen/a.png'))
        self.knight_image_walk_level_four = Widget()
        self.knight_image_sit_level_four = Widget()
        self.knight_image_sit_up_level_four = Widget()

        self.knight_box_level_four = BoxLayout(padding=(x * 2.2, y * 4, x * 2.8, y * 3))

        self.animation_frag_box_level_four = BoxLayout(padding=(x*5.5, -y * 9.5, -x, y * 16.2))
        self.animation_frag_image_box_level_four = BoxLayout(padding=(x, -y * 6.5, 0, y * 10.5))
        self.frags_animation_level_four = Widget()
        self.but_text = Image(source=('Design Screen/disk.zip'), anim_delay=.01, keep_ratio=False, allow_stretch=True,
                  keep_data=False)
        self.tangle_text_but = 89.0
        self.animation_frag_box_level_four.add_widget(self.but_text)
        self.animation_frag_image_box_level_four.add_widget(self.frags_animation_level_four)
        self.frages_box_level_four = BoxLayout(padding=(x * 3, -y * 14.8, x * 2.5, y * 22))
        self.frages_box_image_level_four = BoxLayout(padding=(x * 2.8, -y * 15.1, x * 1.4, y * 21.8))
        self.frages_box_image_level_four.add_widget(
            Image(source=('Design Screen/disk.zip'), anim_delay=.01, keep_ratio=False, allow_stretch=True,
                  keep_data=False))
        self.frag_level_four = Widget()
        self.frages_box_level_four_down = BoxLayout(padding=(x * 2, 0, x * 3.5, y * 6))
        self.frages_box_image_level_four_down = BoxLayout(padding=(x * 2, 0, x * 3.5, y * 6))
        self.frages_box_image_level_four_down.add_widget(
            Image(source=('Design Screen/стрела.zip'), anim_delay=.1, keep_ratio=False, allow_stretch=True))
        self.frag_level_four_down = Widget()
        self.frages_box_image_level_four_down.y = self.knight_box_level_four.y + y * 58
        self.frages_box_level_four_down.y = self.knight_box_level_four.y + y * 58
        self.frages_box_level_four_down.add_widget(self.frag_level_four_down)
        self.frages_box_level_four.add_widget(self.frag_level_four)
        self.word_box_level_four = BoxLayout(padding=(x_level * 1.5, -y * 13, x_level * 2, y * 20))
        self.word_image_level_four = Image(source=('Design Screen/буквы/буква G.png'))
        self.word_box_level_four.add_widget(self.word_image_level_four)
        self.Knight_box_letter_level_four = BoxLayout(padding=(x_level * 0.2, y * 0.6, x_level * 2, y * 7))
        self.Knight_image_box_letter_level_four = Image(source=('Design Screen/буквы/KNIGHT_4_level.png'))
        self.Knight_box_letter_level_four.add_widget(self.Knight_image_box_letter_level_four)
        self.Knight_box_letter_level_four_empty = BoxLayout(padding=(x_level * 0.2, y * 0.6, x_level * 2, y * 7))
        self.knight_box_button_level_four = Widget()
        self.knight_box_level_four.add_widget(self.knight_box_button_level_four)
        self.knight_image_box_level_four.add_widget(self.knight_image_start_level_four)
        self.knight_level_four_complete_box = BoxLayout(padding=(x * 2.5, -y * 26.5, x * 0.5, y * 26.5))
        self.knight_level_four_complete_box.add_widget(
            Image(source=('Design Screen/end_level_animation.zip'), anim_delay=.018, allow_stretch=False,
                  keep_ratio=False))
        self.climb_screen_level_four.add_widget(self.knight_level_four_complete_box)
        self.climb_screen_level_four.add_widget(self.wall_box_level_four)
        self.climb_screen_level_four.add_widget(self.frages_box_level_four_down)
        self.climb_screen_level_four.add_widget(self.frages_box_image_level_four_down)
        self.climb_screen_level_four.add_widget(self.frages_box_level_four)
        self.climb_screen_level_four.add_widget(self.frages_box_image_level_four)
        self.climb_screen_level_four.add_widget(self.animation_frag_box_level_four)
        self.climb_screen_level_four.add_widget(self.animation_frag_image_box_level_four)
        self.climb_screen_level_four.add_widget(self.knight_box_level_four)
        self.climb_screen_level_four.add_widget(self.knight_image_box_level_four)
        self.climb_screen_level_four.add_widget(self.word_box_level_four)
        for i in self.coin_boxes_level_four[:]:
            self.climb_screen_level_four.add_widget(i)
        self.four_level_screen_child.add_widget(self.sky_box_level_four)
        self.four_level_screen_child.add_widget(self.climb_screen_level_four)
        self.four_level_screen.add_widget(self.four_level_screen_child)

        self.swipe_level_four = Slider(min=-1, max=1, value=0, step=.5, background_width=(0), cursor_size=(0, 0),
                                        on_touch_up=self.on_touch_up, on_touch_move=self.on_touch_move,
                                        on_touch_down=self.on_touch_down)
        self.four_level.add_widget(self.four_level_screen)

        "_____________________________________________________________________________________________________________"
        # ......................................................................................добавляем пятый уровень
        self.five_level = Screen(name=('Five_level'))
        self.five_level_screen = RelativeLayout()
        self.five_level_screen_child = RelativeLayout()
        self.climb_screen_level_five = RelativeLayout()
        self.sky_box_level_five = BoxLayout(padding=(-x*10, -y*4, -x*10, -y*8))
        self.sky_image_level_five = Image(source=('Design Screen/небо.png'), allow_stretch=True,
                                          keep_ratio=False)
        self.sky_box_level_five.add_widget(self.sky_image_level_five)

        self.wall_box_level_five = BoxLayout(padding=(0, -y * 24, 0, 0))
        self.climb_wall_level_five = Image(source=('Design Screen/фон_стена_дерево_3.png'), allow_stretch=True,
                                           keep_ratio=False)

        self.wall_box_level_five.add_widget(self.climb_wall_level_five)


        self.coin_box_level_five_1 = AnchorLayout(padding=(x_level * 1.5, 0, x_level * 2, y * 7))
        self.coin_box_level_five_2 = AnchorLayout(padding=(x_level * 1.5, -y, x_level * 2, y * 8))
        self.coin_box_level_five_3 = AnchorLayout(padding=(x_level * 1.5, -y * 2, x_level * 2, y * 9))
        self.coin_box_level_five_4 = AnchorLayout(padding=(x_level * 1.5, -y * 5, x_level * 2, y * 12))
        self.coin_box_level_five_5 = AnchorLayout(padding=(x_level * 1.5, -y * 6, x_level * 2, y * 13))
        self.coin_box_level_five_6 = AnchorLayout(padding=(x_level * 1.5, -y * 7, x_level * 2, y * 14))
        self.coin_box_level_five_7 = AnchorLayout(padding=(x_level * 1.5, -y * 10, x_level * 2, y * 17))
        self.coin_box_level_five_8 = AnchorLayout(padding=(x_level * 0.5, -y * 11, x_level * 3, y * 18))
        self.coin_box_level_five_9 = AnchorLayout(padding=(x_level * 1.5, -y * 12, x_level * 2, y * 19))
        self.coin_box_level_five_10 = AnchorLayout(padding=(x_level * 1.5, -y * 14, x_level * 2, y * 21))
        self.coin_box_level_five_11 = AnchorLayout(padding=(x_level * 0.5, -y * 15, x_level * 3, y * 22))
        self.coin_box_level_five_12 = AnchorLayout(padding=(x_level * 1.5, -y * 16, x_level * 2, y * 23))

        self.coin_boxes_level_five = [self.coin_box_level_five_1, self.coin_box_level_five_2,
                                      self.coin_box_level_five_3,
                                      self.coin_box_level_five_4, self.coin_box_level_five_5,
                                      self.coin_box_level_five_6,
                                      self.coin_box_level_five_7, self.coin_box_level_five_8,
                                      self.coin_box_level_five_9,
                                      self.coin_box_level_five_10, self.coin_box_level_five_11,
                                      self.coin_box_level_five_12]

        self.coins_level_five = []

        self.coin_check_level_five = 0

        for i in range(12):
            i = Coin()
            self.coins_level_five.append(i)

        for a in self.coin_boxes_level_five[:]:
            a.add_widget(self.coins_level_five[self.coin_check_level_five])
            self.coin_check_level_five += 1

        self.coin_count_level_five = 0

        self.knight_image_box_level_five = BoxLayout(padding=(-x,0,x/1.5,0))

        self.knight_image_jump_level_five = Widget()
        self.knight_image_end_level_five = Widget()
        self.knight_image_start_level_five = Image(source=('Design Screen/a.png'))
        self.knight_image_walk_level_five = Widget()
        self.knight_image_sit_level_five = Widget()
        self.knight_image_sit_up_level_five = Widget()

        self.knight_box_level_five = BoxLayout(padding=(x * 2.2, y * 4, x * 2.8, y * 3))
        self.frages_box_level_five = BoxLayout(padding=(x * 3, -y * 14.8, x * 2.5, y * 22))
        self.frages_box_image_level_five = BoxLayout(padding=(x * 2.8, -y * 15.1, x * 1.4, y * 21.8))
        self.frages_box_image_level_five.add_widget(
            Image(source=('Design Screen/disk.zip'), anim_delay=.01, keep_ratio=False, allow_stretch=True))
        self.frag_level_five = Widget()
        self.frages_box_level_five_down = BoxLayout(padding=(x * 2, 0, x * 3.5, y * 6))
        self.frages_box_image_level_five_down = BoxLayout(padding=(x * 2, 0, x * 3.5, y * 6))
        self.frages_box_image_level_five_down.add_widget(
            Image(source=('Design Screen/стрела.zip'), anim_delay=.1, keep_ratio=False, allow_stretch=True))
        self.frag_level_five_down = Widget()
        self.frages_box_image_level_five_down.y = self.knight_box_level_five.y + y * 64
        self.frages_box_level_five_down.y = self.knight_box_level_five.y + y * 64
        self.frages_box_level_five_down.add_widget(self.frag_level_five_down)
        self.frages_box_level_five.add_widget(self.frag_level_five)


        self.frag_kick_level_five = AnchorLayout(padding=(x * 2.8, -y * 5.3, x * 1.4, y * 12))
        self.frag_kicker_level_five = Image(source=('Design Screen/disk.zip'), anim_delay=.01, keep_ratio=False,
                                                  allow_stretch=True)
        self.frag_kicker_true_level_five = Widget()
        self.frag_kick_level_five.add_widget(self.frag_kicker_level_five)
        self.frag_kick_level_five.add_widget(self.frag_kicker_true_level_five)


        self.word_box_level_five = BoxLayout(padding=(x_level * 1.5, -y * 13, x_level * 2, y * 20))
        self.word_image_level_five = Image(source=('Design Screen/буквы/буква H.png'))
        self.word_box_level_five.add_widget(self.word_image_level_five)
        self.Knight_box_letter_level_five = BoxLayout(padding=(x_level * 0.2, y * 0.6, x_level * 2, y * 7))
        self.Knight_image_box_letter_level_five = Image(source=('Design Screen/буквы/KNIGHT_5_level.png'))
        self.Knight_box_letter_level_five.add_widget(self.Knight_image_box_letter_level_five)
        self.Knight_box_letter_level_five_empty = BoxLayout(padding=(x_level * 0.2, y * 0.6, x_level * 2, y * 7))
        self.knight_box_button_level_five = Widget()
        self.knight_box_level_five.add_widget(self.knight_box_button_level_five)
        self.knight_image_box_level_five.add_widget(self.knight_image_start_level_five)
        self.knight_level_five_complete_box = BoxLayout(padding=(x * 2.5, -y * 26.5, x * 0.5, y * 26.5))
        self.knight_level_five_complete_box.add_widget(
            Image(source=('Design Screen/end_level_animation.zip'), anim_delay=.018, allow_stretch=False,
                  keep_ratio=False))
        self.climb_screen_level_five.add_widget(self.knight_level_five_complete_box)
        self.climb_screen_level_five.add_widget(self.wall_box_level_five)
        self.climb_screen_level_five.add_widget(self.frages_box_level_five_down)
        self.climb_screen_level_five.add_widget(self.frages_box_image_level_five_down)
        self.climb_screen_level_five.add_widget(self.frages_box_level_five)
        self.climb_screen_level_five.add_widget(self.frages_box_image_level_five)
        self.climb_screen_level_five.add_widget(self.frag_kick_level_five)
        self.climb_screen_level_five.add_widget(self.knight_box_level_five)
        self.climb_screen_level_five.add_widget(self.knight_image_box_level_five)
        self.climb_screen_level_five.add_widget(self.word_box_level_five)
        for i in self.coin_boxes_level_five[:]:
            self.climb_screen_level_five.add_widget(i)
        self.five_level_screen_child.add_widget(self.sky_box_level_five)
        self.five_level_screen_child.add_widget(self.climb_screen_level_five)
        self.five_level_screen.add_widget(self.five_level_screen_child)

        self.swipe_level_five = Slider(min=-1, max=1, value=0, step=.5, background_width=(0), cursor_size=(0, 0),
                                       on_touch_up=self.on_touch_up, on_touch_move=self.on_touch_move,
                                       on_touch_down=self.on_touch_down)
        self.five_level.add_widget(self.five_level_screen)


        "_____________________________________________________________________________________________________________"
        # ......................................................................................добавляем шестой уровень
        self.six_level = Screen(name=('Six_level'))
        self.six_level_screen = RelativeLayout()
        self.six_level_screen_child = RelativeLayout()
        self.climb_screen_level_six = RelativeLayout()
        self.sky_box_level_six = BoxLayout(padding=(-x * 10, -y * 4, -x * 10, -y * 8))
        self.sky_image_level_six = Image(source=('Design Screen/небо.png'), allow_stretch=True,
                                          keep_ratio=False)
        self.sky_box_level_six.add_widget(self.sky_image_level_six)
        self.ran_image_level_six = Image(source=('Design Screen/дождь.zip'), anim_delay=.1, allow_stretch=True,
                                          keep_ratio=False)

        self.wall_box_level_six = BoxLayout(padding=(0, -y * 24, 0, 0))
        self.climb_wall_level_six = Image(source=('Design Screen/фон_стена_дерево_3.png'), allow_stretch=True,
                                           keep_ratio=False)

        self.wall_box_level_six.add_widget(self.climb_wall_level_six)

        self.coin_box_level_six_1 = AnchorLayout(padding=(x_level * 1.5, 0, x_level * 2, y * 7))
        self.coin_box_level_six_2 = AnchorLayout(padding=(x_level * 0.5, -y, x_level * 3, y * 8))
        self.coin_box_level_six_3 = AnchorLayout(padding=(x_level * 1.5, -y * 2, x_level * 2, y * 9))
        self.coin_box_level_six_4 = AnchorLayout(padding=(x_level * 1.5, -y * 4, x_level * 2, y * 11))
        self.coin_box_level_six_5 = AnchorLayout(padding=(x_level * 0.5, -y * 5, x_level * 3, y * 12))
        self.coin_box_level_six_6 = AnchorLayout(padding=(x_level * 1.5, -y * 6, x_level * 2, y * 13))
        self.coin_box_level_six_7 = AnchorLayout(padding=(x_level * 1.5, -y * 10, x_level * 2, y * 17))
        self.coin_box_level_six_8 = AnchorLayout(padding=(x_level * 0.5, -y * 11, x_level * 3, y * 18))
        self.coin_box_level_six_9 = AnchorLayout(padding=(x_level * 1.5, -y * 12, x_level * 2, y * 19))
        self.coin_box_level_six_10 = AnchorLayout(padding=(x_level * 1.5, -y * 14, x_level * 2, y * 21))
        self.coin_box_level_six_11 = AnchorLayout(padding=(x_level * 0.5, -y * 15, x_level * 3, y * 22))
        self.coin_box_level_six_12 = AnchorLayout(padding=(x_level * 1.5, -y * 16, x_level * 2, y * 23))

        self.coin_boxes_level_six = [self.coin_box_level_six_1, self.coin_box_level_six_2,
                                      self.coin_box_level_six_3,
                                      self.coin_box_level_six_4, self.coin_box_level_six_5,
                                      self.coin_box_level_six_6,
                                      self.coin_box_level_six_7, self.coin_box_level_six_8,
                                      self.coin_box_level_six_9,
                                      self.coin_box_level_six_10, self.coin_box_level_six_11,
                                      self.coin_box_level_six_12]

        self.coins_level_six = []

        self.coin_check_level_six = 0

        for i in range(12):
            i = Coin()
            self.coins_level_six.append(i)

        for a in self.coin_boxes_level_six[:]:
            a.add_widget(self.coins_level_six[self.coin_check_level_six])
            self.coin_check_level_six += 1

        self.coin_count_level_six = 0

        self.knight_image_box_level_six = BoxLayout(padding=(-x, 0, x / 1.5, 0))

        self.knight_image_jump_level_six = Widget()
        self.knight_image_end_level_six = Widget()
        self.knight_image_start_level_six = Image(source=('Design Screen/a.png'))
        self.knight_image_walk_level_six = Widget()
        self.knight_image_sit_level_six = Widget()
        self.knight_image_sit_up_level_six = Widget()
        self.knight_box_level_six = BoxLayout(padding=(x * 2.2, y * 4, x * 2.8, y * 3))

        self.frages_box_level_six_down = BoxLayout(padding=(x * 2, 0, x * 3.5, y * 6))
        self.frages_box_image_level_six_down = BoxLayout(padding=(x * 2, 0, x * 3.5, y * 6))
        self.frages_box_image_level_six_down.add_widget(
            Image(source=('Design Screen/стрела.zip'), anim_delay=.1, keep_ratio=False, allow_stretch=True))
        self.frag_level_six_down = Widget()
        self.frages_box_image_level_six_down.y = self.knight_box_level_six.y + y * 64
        self.frages_box_level_six_down.y = self.knight_box_level_six.y + y * 64
        self.frages_box_level_six_down.add_widget(self.frag_level_six_down)

        self.frag_kick_level_six = AnchorLayout(padding=(x * 2.8, -y * 3.3, x * 1.4, y * 10))
        self.frag_kicker_level_six = Image(source=('Design Screen/disk.zip'), anim_delay=.01, keep_ratio=False,
                                                  allow_stretch=True)
        self.frag_kicker_true_level_six = Widget(size_hint=(.5, .5))
        self.frag_kick_level_six.add_widget(self.frag_kicker_level_six)
        self.frag_kick_level_six.add_widget(self.frag_kicker_true_level_six)

        self.frag_1_kick_level_six = AnchorLayout(padding=(x * 2.8, -y * 8.3, x * 1.4, y * 15))
        self.frag_1_kicker_level_six = Image(source=('Design Screen/disk.zip'), anim_delay=.01, keep_ratio=False,
                                           allow_stretch=True)
        self.frag_1_kicker_true_level_six = Widget(size_hint=(.5, .5))
        self.frag_1_kick_level_six.add_widget(self.frag_1_kicker_level_six)
        self.frag_1_kick_level_six.add_widget(self.frag_1_kicker_true_level_six)

        self.frag_2_kick_level_six = AnchorLayout(padding=(x * 2.8, -y * 13.3, x * 1.4, y * 20))
        self.frag_2_kicker_level_six = Image(source=('Design Screen/disk.zip'), anim_delay=.01, keep_ratio=False,
                                           allow_stretch=True)
        self.frag_2_kicker_true_level_six = Widget(size_hint=(.5, .5))
        self.frag_2_kick_level_six.add_widget(self.frag_2_kicker_level_six)
        self.frag_2_kick_level_six.add_widget(self.frag_2_kicker_true_level_six)

        self.word_box_level_six = BoxLayout(padding=(x_level * 0.5, -y * 13, x_level * 3, y * 20))
        self.word_image_level_six = Image(source=('Design Screen/буквы/буква T.png'))
        self.word_box_level_six.add_widget(self.word_image_level_six)
        self.Knight_box_letter_level_six = BoxLayout(padding=(x_level * 0.2, y * 0.6, x_level * 2, y * 7))
        self.Knight_image_box_letter_level_six = Image(source=('Design Screen/буквы/KNIGHT_6_level.png'))
        self.Knight_box_letter_level_six.add_widget(self.Knight_image_box_letter_level_six)
        self.Knight_box_letter_level_six_empty = BoxLayout(padding=(x_level * 0.2, y * 0.6, x_level * 2, y * 7))
        self.knight_box_button_level_six = Widget()
        self.knight_box_level_six.add_widget(self.knight_box_button_level_six)
        self.knight_image_box_level_six.add_widget(self.knight_image_start_level_six)
        self.knight_level_six_complete_box = BoxLayout(padding=(0, -y * 28.5, 0, y * 28))
        self.knight_level_six_complete_video = Image(source=('Design Screen/end_level_animation_6.zip'), anim_delay= 0.03, allow_stretch=True,
                  keep_ratio=False, anim_loop = 1)
        self.knight_level_six_complete_box.add_widget(self.knight_level_six_complete_video)
        self.climb_screen_level_six.add_widget(self.knight_level_six_complete_box)
        self.climb_screen_level_six.add_widget(self.wall_box_level_six)
        self.climb_screen_level_six.add_widget(self.frages_box_level_six_down)
        self.climb_screen_level_six.add_widget(self.frages_box_image_level_six_down)
        self.climb_screen_level_six.add_widget(self.frag_kick_level_six)
        self.climb_screen_level_six.add_widget(self.frag_1_kick_level_six)
        self.climb_screen_level_six.add_widget(self.frag_2_kick_level_six)
        self.climb_screen_level_six.add_widget(self.knight_box_level_six)
        self.climb_screen_level_six.add_widget(self.knight_image_box_level_six)
        self.climb_screen_level_six.add_widget(self.word_box_level_six)
        for i in self.coin_boxes_level_six[:]:
            self.climb_screen_level_six.add_widget(i)
        self.six_level_screen_child.add_widget(self.sky_box_level_six)
        self.six_level_screen_child.add_widget(self.climb_screen_level_six)
        self.six_level_screen.add_widget(self.six_level_screen_child)

        self.swipe_level_six = Slider(min=-1, max=1, value=0, step=.5, background_width=(0), cursor_size=(0, 0),
                                       on_touch_up=self.on_touch_up, on_touch_move=self.on_touch_move,
                                       on_touch_down=self.on_touch_down)
        self.six_level.add_widget(self.six_level_screen)


        "_____________________________________________________________________________________________________________"
        # ......................................................................................добавляем седьмой уровень
        self.seven_level = Screen(name=('Seven_level'))
        self.seven_level_screen = RelativeLayout()
        self.seven_level_screen_child = RelativeLayout()
        self.climb_screen_level_seven = RelativeLayout()
        self.sky_box_level_seven = BoxLayout(padding=(-x * 10, -y * 4, -x * 10, -y * 8))
        self.sky_image_level_seven = Image(source=('Design Screen/небо.png'), allow_stretch=True,
                                         keep_ratio=False)
        self.sky_box_level_seven.add_widget(self.sky_image_level_seven)

        self.wall_box_level_seven = BoxLayout(padding=(0, -y * 24, 0, 0))
        self.climb_wall_level_seven = Image(source=('Design Screen/фон_стена_дерево_3.png'), allow_stretch=True,
                                          keep_ratio=False)

        self.wall_box_level_seven.add_widget(self.climb_wall_level_seven)

        self.coin_box_level_seven_1 = AnchorLayout(padding=(x_level * 1.5, 0, x_level * 2, y * 7))
        self.coin_box_level_seven_2 = AnchorLayout(padding=(x_level * 0.5, -y, x_level * 3, y * 8))
        self.coin_box_level_seven_3 = AnchorLayout(padding=(x_level * 1.5, -y * 2, x_level * 2, y * 9))
        self.coin_box_level_seven_4 = AnchorLayout(padding=(x_level * 1.5, -y * 4, x_level * 2, y * 11))
        self.coin_box_level_seven_5 = AnchorLayout(padding=(x_level * 0.5, -y * 5, x_level * 3, y * 12))
        self.coin_box_level_seven_6 = AnchorLayout(padding=(x_level * 1.5, -y * 6, x_level * 2, y * 13))
        self.coin_box_level_seven_7 = AnchorLayout(padding=(x_level * 1.5, -y * 10, x_level * 2, y * 17))
        self.coin_box_level_seven_8 = AnchorLayout(padding=(x_level * 0.5, -y * 11, x_level * 3, y * 18))
        self.coin_box_level_seven_9 = AnchorLayout(padding=(x_level * 1.5, -y * 12, x_level * 2, y * 19))
        self.coin_box_level_seven_10 = AnchorLayout(padding=(x_level * 1.5, -y * 14, x_level * 2, y * 21))
        self.coin_box_level_seven_11 = AnchorLayout(padding=(x_level * 0.5, -y * 15, x_level * 3, y * 22))
        self.coin_box_level_seven_12 = AnchorLayout(padding=(x_level * 1.5, -y * 16, x_level * 2, y * 23))

        self.coin_boxes_level_seven = [self.coin_box_level_seven_1, self.coin_box_level_seven_2,
                                     self.coin_box_level_seven_3,
                                     self.coin_box_level_seven_4, self.coin_box_level_seven_5,
                                     self.coin_box_level_seven_6,
                                     self.coin_box_level_seven_7, self.coin_box_level_seven_8,
                                     self.coin_box_level_seven_9,
                                     self.coin_box_level_seven_10, self.coin_box_level_seven_11,
                                     self.coin_box_level_seven_12]

        self.coins_level_seven = []

        self.coin_check_level_seven = 0

        for i in range(12):
            i = Widget()
            self.coins_level_seven.append(i)

        for a in self.coin_boxes_level_seven[:]:
            a.add_widget(self.coins_level_seven[self.coin_check_level_seven])
            self.coin_check_level_seven += 1

        self.coin_count_level_seven = 0

        self.knight_image_box_level_seven = BoxLayout(padding=(-x, 0, x / 1.5, 0))

        self.knight_image_jump_level_seven = Widget()
        self.knight_image_end_level_seven = Widget()
        self.knight_image_start_level_seven = Image(source=('Design Screen/a.png'))
        self.knight_image_walk_level_seven = Widget()
        self.knight_image_sit_level_seven = Widget()
        self.knight_image_sit_up_level_seven = Widget()
        self.knight_box_level_seven = BoxLayout(padding=(x * 2.2, y * 4, x * 2.8, y * 3))

        self.frages_box_level_seven_down = BoxLayout(padding=(x * 2, 0, x * 3.5, y * 6))
        self.frages_box_image_level_seven_down = BoxLayout(padding=(x * 2, 0, x * 3.5, y * 6))
        self.frages_box_image_level_seven_down.add_widget(
            Image(source=('Design Screen/стрела.zip'), anim_delay=.1, keep_ratio=False, allow_stretch=True))
        self.frag_level_seven_down = Widget()
        self.frages_box_image_level_seven_down.y = self.knight_box_level_seven.y + y * 64
        self.frages_box_level_seven_down.y = self.knight_box_level_seven.y + y * 64
        self.frages_box_level_seven_down.add_widget(self.frag_level_seven_down)

        self.frag_kick_level_seven = AnchorLayout(padding=(x * 2.8, -y * 3.3, x * 1.4, y * 10))
        self.frag_kicker_level_seven = Image(source=('Design Screen/disk.zip'), anim_delay=.01, keep_ratio=False,
                                           allow_stretch=True)
        self.frag_kicker_true_level_seven = Widget(size_hint=(.5, .5))
        self.frag_kick_level_seven.add_widget(self.frag_kicker_level_seven)
        self.frag_kick_level_seven.add_widget(self.frag_kicker_true_level_seven)

        self.frag_1_kick_level_seven = AnchorLayout(padding=(x * 2.8, -y * 8.3, x * 1.4, y * 15))
        self.frag_1_kicker_level_seven = Image(source=('Design Screen/disk.zip'), anim_delay=.01, keep_ratio=False,
                                             allow_stretch=True)
        self.frag_1_kicker_true_level_seven = Widget(size_hint=(.5, .5))
        self.frag_1_kick_level_seven.add_widget(self.frag_1_kicker_level_seven)
        self.frag_1_kick_level_seven.add_widget(self.frag_1_kicker_true_level_seven)

        self.frag_2_kick_level_seven = AnchorLayout(padding=(x * 2.8, -y * 13.3, x * 1.4, y * 20))
        self.frag_2_kicker_level_seven = Image(source=('Design Screen/disk.zip'), anim_delay=.01, keep_ratio=False,
                                             allow_stretch=True)
        self.frag_2_kicker_true_level_seven = Widget(size_hint=(.5, .5))
        self.frag_2_kick_level_seven.add_widget(self.frag_2_kicker_level_seven)
        self.frag_2_kick_level_seven.add_widget(self.frag_2_kicker_true_level_seven)

        self.word_box_level_seven = BoxLayout(padding=(x_level * 0.5, -y * 13, x_level * 3, y * 20))
        self.word_image_level_seven = Image(source=('Design Screen/буквы/буква L.png'))
        self.word_box_level_seven.add_widget(self.word_image_level_seven)
        self.Knight_box_letter_level_seven = BoxLayout(padding=(x_level * 0.2, y * 0.6, x_level * 2, y * 7))
        self.Knight_image_box_letter_level_seven = Image(source=('Design Screen/буквы/KNIGHT_7_level.png'))
        self.Knight_box_letter_level_seven.add_widget(self.Knight_image_box_letter_level_seven)
        self.Knight_box_letter_level_seven_empty = BoxLayout(padding=(x_level * 0.2, y * 0.6, x_level * 2, y * 7))
        self.knight_box_button_level_seven = Widget()
        self.knight_box_level_seven.add_widget(self.knight_box_button_level_seven)
        self.knight_image_box_level_seven.add_widget(self.knight_image_start_level_seven)
        self.knight_level_seven_complete_box = BoxLayout(padding=(0, -y * 28.5, 0, y * 28))
        self.knight_level_seven_complete_video = Image(source=('Design Screen/end_level_animation_2.zip'),
                                                     anim_delay=0.03, allow_stretch=True,
                                                     keep_ratio=False, anim_loop=1)
        self.knight_level_seven_complete_box.add_widget(self.knight_level_seven_complete_video)
        self.climb_screen_level_seven.add_widget(self.knight_level_seven_complete_box)
        self.climb_screen_level_seven.add_widget(self.wall_box_level_seven)
        self.climb_screen_level_seven.add_widget(self.frages_box_level_seven_down)
        self.climb_screen_level_seven.add_widget(self.frages_box_image_level_seven_down)
        self.climb_screen_level_seven.add_widget(self.frag_kick_level_seven)
        self.climb_screen_level_seven.add_widget(self.frag_1_kick_level_seven)
        self.climb_screen_level_seven.add_widget(self.frag_2_kick_level_seven)
        self.climb_screen_level_seven.add_widget(self.knight_box_level_seven)
        self.climb_screen_level_seven.add_widget(self.knight_image_box_level_seven)
        self.climb_screen_level_seven.add_widget(self.word_box_level_seven)
        for i in self.coin_boxes_level_seven[:]:
            self.climb_screen_level_seven.add_widget(i)
        self.seven_level_screen_child.add_widget(self.sky_box_level_seven)
        self.seven_level_screen_child.add_widget(self.climb_screen_level_seven)
        self.seven_level_screen.add_widget(self.seven_level_screen_child)

        self.swipe_level_seven = Slider(min=-1, max=1, value=0, step=.5, background_width=(0), cursor_size=(0, 0),
                                      on_touch_up=self.on_touch_up, on_touch_move=self.on_touch_move,
                                      on_touch_down=self.on_touch_down)
        self.seven_level.add_widget(self.seven_level_screen)

        "___________________________________________________________________________________________________________"

        "_____________________________________________________________________________________________________________"
        # ......................................................................................добавляем восьмой уровень
        self.eight_level = Screen(name=('Eight_level'))
        self.eight_level_screen = RelativeLayout()
        self.eight_level_screen_child = RelativeLayout()
        self.climb_screen_level_eight = RelativeLayout()
        self.sky_box_level_eight = BoxLayout(padding=(-x * 10, -y * 4, -x * 10, -y * 8))
        self.sky_image_level_eight = Image(source=('Design Screen/небо.png'), allow_stretch=True,
                                           keep_ratio=False)
        self.sky_box_level_eight.add_widget(self.sky_image_level_eight)

        self.wall_box_level_eight = BoxLayout(padding=(0, -y * 24, 0, 0))
        self.climb_wall_level_eight = Image(source=('Design Screen/фон_стена_дерево_3.png'), allow_stretch=True,
                                            keep_ratio=False)

        self.wall_box_level_eight.add_widget(self.climb_wall_level_eight)

        self.coin_box_level_eight_1 = AnchorLayout(padding=(x_level * 1.5, 0, x_level * 2, y * 7))
        self.coin_box_level_eight_2 = AnchorLayout(padding=(x_level * 0.5, -y, x_level * 3, y * 8))
        self.coin_box_level_eight_3 = AnchorLayout(padding=(x_level * 1.5, -y * 2, x_level * 2, y * 9))
        self.coin_box_level_eight_4 = AnchorLayout(padding=(x_level * 1.5, -y * 4, x_level * 2, y * 11))
        self.coin_box_level_eight_5 = AnchorLayout(padding=(x_level * 0.5, -y * 5, x_level * 3, y * 12))
        self.coin_box_level_eight_6 = AnchorLayout(padding=(x_level * 1.5, -y * 6, x_level * 2, y * 13))
        self.coin_box_level_eight_7 = AnchorLayout(padding=(x_level * 1.5, -y * 10, x_level * 2, y * 17))
        self.coin_box_level_eight_8 = AnchorLayout(padding=(x_level * 0.5, -y * 11, x_level * 3, y * 18))
        self.coin_box_level_eight_9 = AnchorLayout(padding=(x_level * 1.5, -y * 12, x_level * 2, y * 19))
        self.coin_box_level_eight_10 = AnchorLayout(padding=(x_level * 1.5, -y * 14, x_level * 2, y * 21))
        self.coin_box_level_eight_11 = AnchorLayout(padding=(x_level * 0.5, -y * 15, x_level * 3, y * 22))
        self.coin_box_level_eight_12 = AnchorLayout(padding=(x_level * 1.5, -y * 16, x_level * 2, y * 23))

        self.coin_boxes_level_eight = [self.coin_box_level_eight_1, self.coin_box_level_eight_2,
                                       self.coin_box_level_eight_3,
                                       self.coin_box_level_eight_4, self.coin_box_level_eight_5,
                                       self.coin_box_level_eight_6,
                                       self.coin_box_level_eight_7, self.coin_box_level_eight_8,
                                       self.coin_box_level_eight_9,
                                       self.coin_box_level_eight_10, self.coin_box_level_eight_11,
                                       self.coin_box_level_eight_12]

        self.coins_level_eight = []

        self.coin_check_level_eight = 0

        for i in range(12):
            i = Widget()
            self.coins_level_eight.append(i)

        for a in self.coin_boxes_level_eight[:]:
            a.add_widget(self.coins_level_eight[self.coin_check_level_eight])
            self.coin_check_level_eight += 1

        self.coin_count_level_eight = 0

        self.knight_image_box_level_eight = BoxLayout(padding=(-x, 0, x / 1.5, 0))

        self.knight_image_jump_level_eight = Widget()
        self.knight_image_end_level_eight = Widget()
        self.knight_image_start_level_eight = Image(source=('Design Screen/a.png'))
        self.knight_image_walk_level_eight = Widget()
        self.knight_image_sit_level_eight = Widget()
        self.knight_image_sit_up_level_eight = Widget()
        self.knight_box_level_eight = BoxLayout(padding=(x * 2.2, y * 4, x * 2.8, y * 3))

        self.frages_box_level_eight_down = BoxLayout(padding=(x * 2, 0, x * 3.5, y * 6))
        self.frages_box_image_level_eight_down = BoxLayout(padding=(x * 2, 0, x * 3.5, y * 6))
        self.frages_box_image_level_eight_down.add_widget(
            Image(source=('Design Screen/стрела.zip'), anim_delay=.1, keep_ratio=False, allow_stretch=True))
        self.frag_level_eight_down = Widget()
        self.frages_box_image_level_eight_down.y = self.knight_box_level_eight.y + y * 64
        self.frages_box_level_eight_down.y = self.knight_box_level_eight.y + y * 64
        self.frages_box_level_eight_down.add_widget(self.frag_level_eight_down)

        self.frag_kick_level_eight = AnchorLayout(padding=(x * 2.8, -y * 3.3, x * 1.4, y * 10))
        self.frag_kicker_level_eight = Image(source=('Design Screen/disk.zip'), anim_delay=.01, keep_ratio=False,
                                             allow_stretch=True)
        self.frag_kicker_true_level_eight = Widget(size_hint=(.5, .5))
        self.frag_kick_level_eight.add_widget(self.frag_kicker_level_eight)
        self.frag_kick_level_eight.add_widget(self.frag_kicker_true_level_eight)

        self.frag_1_kick_level_eight = AnchorLayout(padding=(x * 2.8, -y * 8.3, x * 1.4, y * 15))
        self.frag_1_kicker_level_eight = Image(source=('Design Screen/disk.zip'), anim_delay=.01, keep_ratio=False,
                                               allow_stretch=True)
        self.frag_1_kicker_true_level_eight = Widget(size_hint=(.5, .5))
        self.frag_1_kick_level_eight.add_widget(self.frag_1_kicker_level_eight)
        self.frag_1_kick_level_eight.add_widget(self.frag_1_kicker_true_level_eight)

        self.frag_2_kick_level_eight = AnchorLayout(padding=(x * 2.8, -y * 13.3, x * 1.4, y * 20))
        self.frag_2_kicker_level_eight = Image(source=('Design Screen/disk.zip'), anim_delay=.01, keep_ratio=False,
                                               allow_stretch=True)
        self.frag_2_kicker_true_level_eight = Widget(size_hint=(.5, .5))
        self.frag_2_kick_level_eight.add_widget(self.frag_2_kicker_level_eight)
        self.frag_2_kick_level_eight.add_widget(self.frag_2_kicker_true_level_eight)

        self.word_box_level_eight = BoxLayout(padding=(x_level * 0.5, -y * 13, x_level * 3, y * 20))
        self.word_image_level_eight = Image(source=('Design Screen/буквы/буква O.png'))
        self.word_box_level_eight.add_widget(self.word_image_level_eight)
        self.Knight_box_letter_level_eight = BoxLayout(padding=(x_level * 0.2, y * 0.6, x_level * 2, y * 7))
        self.Knight_image_box_letter_level_eight = Image(source=('Design Screen/буквы/KNIGHT_8_level.png'))
        self.Knight_box_letter_level_eight.add_widget(self.Knight_image_box_letter_level_eight)
        self.Knight_box_letter_level_eight_empty = BoxLayout(padding=(x_level * 0.2, y * 0.6, x_level * 2, y * 7))
        self.knight_box_button_level_eight = Widget()
        self.knight_box_level_eight.add_widget(self.knight_box_button_level_eight)
        self.knight_image_box_level_eight.add_widget(self.knight_image_start_level_eight)
        self.knight_level_eight_complete_box = BoxLayout(padding=(0, -y * 28.5, 0, y * 28))
        self.knight_level_eight_complete_video = Image(source=('Design Screen/end_level_animation_3.zip'),
                                                       anim_delay=0.03, allow_stretch=True,
                                                       keep_ratio=False, anim_loop=1)
        self.knight_level_eight_complete_box.add_widget(self.knight_level_eight_complete_video)
        self.climb_screen_level_eight.add_widget(self.knight_level_eight_complete_box)
        self.climb_screen_level_eight.add_widget(self.wall_box_level_eight)
        self.climb_screen_level_eight.add_widget(self.frages_box_level_eight_down)
        self.climb_screen_level_eight.add_widget(self.frages_box_image_level_eight_down)
        self.climb_screen_level_eight.add_widget(self.frag_kick_level_eight)
        self.climb_screen_level_eight.add_widget(self.frag_1_kick_level_eight)
        self.climb_screen_level_eight.add_widget(self.frag_2_kick_level_eight)
        self.climb_screen_level_eight.add_widget(self.knight_box_level_eight)
        self.climb_screen_level_eight.add_widget(self.knight_image_box_level_eight)
        self.climb_screen_level_eight.add_widget(self.word_box_level_eight)
        for i in self.coin_boxes_level_eight[:]:
            self.climb_screen_level_eight.add_widget(i)
        self.eight_level_screen_child.add_widget(self.sky_box_level_eight)
        self.eight_level_screen_child.add_widget(self.climb_screen_level_eight)
        self.eight_level_screen.add_widget(self.eight_level_screen_child)

        self.swipe_level_eight = Slider(min=-1, max=1, value=0, step=.5, background_width=(0), cursor_size=(0, 0),
                                        on_touch_up=self.on_touch_up, on_touch_move=self.on_touch_move,
                                        on_touch_down=self.on_touch_down)
        self.eight_level.add_widget(self.eight_level_screen)

        "___________________________________________________________________________________________________________"

        "_____________________________________________________________________________________________________________"
        # ......................................................................................добавляем девятый уровень
        self.nine_level = Screen(name=('Nine_level'))
        self.nine_level_screen = RelativeLayout()
        self.nine_level_screen_child = RelativeLayout()
        self.climb_screen_level_nine = RelativeLayout()
        self.sky_box_level_nine = BoxLayout(padding=(-x * 10, -y * 4, -x * 10, -y * 8))
        self.sky_image_level_nine = Image(source=('Design Screen/небо.png'), allow_stretch=True,
                                           keep_ratio=False)
        self.sky_box_level_nine.add_widget(self.sky_image_level_nine)

        self.wall_box_level_nine = BoxLayout(padding=(0, -y * 24, 0, 0))
        self.climb_wall_level_nine = Image(source=('Design Screen/фон_стена_дерево_3.png'), allow_stretch=True,
                                            keep_ratio=False)

        self.wall_box_level_nine.add_widget(self.climb_wall_level_nine)

        self.coin_box_level_nine_1 = AnchorLayout(padding=(x_level * 1.5, 0, x_level * 2, y * 7))
        self.coin_box_level_nine_2 = AnchorLayout(padding=(x_level * 0.5, -y, x_level * 3, y * 8))
        self.coin_box_level_nine_3 = AnchorLayout(padding=(x_level * 1.5, -y * 2, x_level * 2, y * 9))
        self.coin_box_level_nine_4 = AnchorLayout(padding=(x_level * 1.5, -y * 4, x_level * 2, y * 11))
        self.coin_box_level_nine_5 = AnchorLayout(padding=(x_level * 0.5, -y * 5, x_level * 3, y * 12))
        self.coin_box_level_nine_6 = AnchorLayout(padding=(x_level * 1.5, -y * 6, x_level * 2, y * 13))
        self.coin_box_level_nine_7 = AnchorLayout(padding=(x_level * 1.5, -y * 10, x_level * 2, y * 17))
        self.coin_box_level_nine_8 = AnchorLayout(padding=(x_level * 0.5, -y * 11, x_level * 3, y * 18))
        self.coin_box_level_nine_9 = AnchorLayout(padding=(x_level * 1.5, -y * 12, x_level * 2, y * 19))
        self.coin_box_level_nine_10 = AnchorLayout(padding=(x_level * 1.5, -y * 14, x_level * 2, y * 21))
        self.coin_box_level_nine_11 = AnchorLayout(padding=(x_level * 0.5, -y * 15, x_level * 3, y * 22))
        self.coin_box_level_nine_12 = AnchorLayout(padding=(x_level * 1.5, -y * 16, x_level * 2, y * 23))

        self.coin_boxes_level_nine = [self.coin_box_level_nine_1, self.coin_box_level_nine_2,
                                       self.coin_box_level_nine_3,
                                       self.coin_box_level_nine_4, self.coin_box_level_nine_5,
                                       self.coin_box_level_nine_6,
                                       self.coin_box_level_nine_7, self.coin_box_level_nine_8,
                                       self.coin_box_level_nine_9,
                                       self.coin_box_level_nine_10, self.coin_box_level_nine_11,
                                       self.coin_box_level_nine_12]

        self.coins_level_nine = []

        self.coin_check_level_nine = 0

        for i in range(12):
            i = Widget()
            self.coins_level_nine.append(i)

        for a in self.coin_boxes_level_nine[:]:
            a.add_widget(self.coins_level_nine[self.coin_check_level_nine])
            self.coin_check_level_nine += 1

        self.coin_count_level_nine = 0

        self.knight_image_box_level_nine = BoxLayout(padding=(-x, 0, x / 1.5, 0))

        self.knight_image_jump_level_nine = Widget()
        self.knight_image_end_level_nine = Widget()
        self.knight_image_start_level_nine = Image(source=('Design Screen/a.png'))
        self.knight_image_walk_level_nine = Widget()
        self.knight_image_sit_level_nine = Widget()
        self.knight_image_sit_up_level_nine = Widget()
        self.knight_box_level_nine = BoxLayout(padding=(x * 2.2, y * 4, x * 2.8, y * 3))

        self.frages_box_level_nine_down = BoxLayout(padding=(x * 2, 0, x * 3.5, y * 6))
        self.frages_box_image_level_nine_down = BoxLayout(padding=(x * 2, 0, x * 3.5, y * 6))
        self.frages_box_image_level_nine_down.add_widget(
            Image(source=('Design Screen/стрела.zip'), anim_delay=.1, keep_ratio=False, allow_stretch=True))
        self.frag_level_nine_down = Widget()
        self.frages_box_image_level_nine_down.y = self.knight_box_level_nine.y + y * 64
        self.frages_box_level_nine_down.y = self.knight_box_level_nine.y + y * 64
        self.frages_box_level_nine_down.add_widget(self.frag_level_nine_down)

        self.frag_kick_level_nine = AnchorLayout(padding=(x * 2.8, -y * 3.3, x * 1.4, y * 10))
        self.frag_kicker_level_nine = Image(source=('Design Screen/disk.zip'), anim_delay=.01, keep_ratio=False,
                                             allow_stretch=True)
        self.frag_kicker_true_level_nine = Widget(size_hint=(.5, .5))
        self.frag_kick_level_nine.add_widget(self.frag_kicker_level_nine)
        self.frag_kick_level_nine.add_widget(self.frag_kicker_true_level_nine)

        self.frag_1_kick_level_nine = AnchorLayout(padding=(x * 2.8, -y * 8.3, x * 1.4, y * 15))
        self.frag_1_kicker_level_nine = Image(source=('Design Screen/disk.zip'), anim_delay=.01, keep_ratio=False,
                                               allow_stretch=True)
        self.frag_1_kicker_true_level_nine = Widget(size_hint=(.5, .5))
        self.frag_1_kick_level_nine.add_widget(self.frag_1_kicker_level_nine)
        self.frag_1_kick_level_nine.add_widget(self.frag_1_kicker_true_level_nine)

        self.frag_2_kick_level_nine = AnchorLayout(padding=(x * 2.8, -y * 13.3, x * 1.4, y * 20))
        self.frag_2_kicker_level_nine = Image(source=('Design Screen/disk.zip'), anim_delay=.01, keep_ratio=False,
                                               allow_stretch=True)
        self.frag_2_kicker_true_level_nine = Widget(size_hint=(.5, .5))
        self.frag_2_kick_level_nine.add_widget(self.frag_2_kicker_level_nine)
        self.frag_2_kick_level_nine.add_widget(self.frag_2_kicker_true_level_nine)

        self.word_box_level_nine = BoxLayout(padding=(x_level * 1.5, -y * 13, x_level * 2, y * 20))
        self.word_image_level_nine = Image(source=('Design Screen/буквы/буква R.png'))
        self.word_box_level_nine.add_widget(self.word_image_level_nine)
        self.Knight_box_letter_level_nine = BoxLayout(padding=(x_level * 0.2, y * 0.6, x_level * 2, y * 7))
        self.Knight_image_box_letter_level_nine = Image(source=('Design Screen/буквы/KNIGHT_9_level.png'))
        self.Knight_box_letter_level_nine.add_widget(self.Knight_image_box_letter_level_nine)
        self.Knight_box_letter_level_nine_empty = BoxLayout(padding=(x_level * 0.2, y * 0.6, x_level * 2, y * 7))
        self.knight_box_button_level_nine = Widget()
        self.knight_box_level_nine.add_widget(self.knight_box_button_level_nine)
        self.knight_image_box_level_nine.add_widget(self.knight_image_start_level_nine)
        self.knight_level_nine_complete_box = BoxLayout(padding=(0, -y * 28.5, 0, y * 28))
        self.knight_level_nine_complete_video = Image(source=('Design Screen/end_level_animation_1.zip'),
                                                       anim_delay=0.03, allow_stretch=True,
                                                       keep_ratio=False, anim_loop=1)
        self.knight_level_nine_complete_box.add_widget(self.knight_level_nine_complete_video)
        self.climb_screen_level_nine.add_widget(self.knight_level_nine_complete_box)
        self.climb_screen_level_nine.add_widget(self.wall_box_level_nine)
        self.climb_screen_level_nine.add_widget(self.frages_box_level_nine_down)
        self.climb_screen_level_nine.add_widget(self.frages_box_image_level_nine_down)
        self.climb_screen_level_nine.add_widget(self.frag_kick_level_nine)
        self.climb_screen_level_nine.add_widget(self.frag_1_kick_level_nine)
        self.climb_screen_level_nine.add_widget(self.frag_2_kick_level_nine)
        self.climb_screen_level_nine.add_widget(self.knight_box_level_nine)
        self.climb_screen_level_nine.add_widget(self.knight_image_box_level_nine)
        self.climb_screen_level_nine.add_widget(self.word_box_level_nine)
        for i in self.coin_boxes_level_nine[:]:
            self.climb_screen_level_nine.add_widget(i)
        self.nine_level_screen_child.add_widget(self.sky_box_level_nine)
        self.nine_level_screen_child.add_widget(self.climb_screen_level_nine)
        self.nine_level_screen.add_widget(self.nine_level_screen_child)

        self.swipe_level_nine = Slider(min=-1, max=1, value=0, step=.5, background_width=(0), cursor_size=(0, 0),
                                        on_touch_up=self.on_touch_up, on_touch_move=self.on_touch_move,
                                        on_touch_down=self.on_touch_down)
        self.nine_level.add_widget(self.nine_level_screen)

        "___________________________________________________________________________________________________________"

        "_____________________________________________________________________________________________________________"
        # ......................................................................................добавляем десятый уровень
        self.ten_level = Screen(name=('Ten_level'))
        self.ten_level_screen = RelativeLayout()
        self.ten_level_screen_child = RelativeLayout()
        self.climb_screen_level_ten = RelativeLayout()
        self.sky_box_level_ten = BoxLayout(padding=(-x * 10, -y * 4, -x * 10, -y * 8))
        self.sky_image_level_ten = Image(source=('Design Screen/небо.png'), allow_stretch=True,
                                           keep_ratio=False)
        self.sky_box_level_ten.add_widget(self.sky_image_level_ten)

        self.wall_box_level_ten = BoxLayout(padding=(0, -y * 24, 0, 0))
        self.climb_wall_level_ten = Image(source=('Design Screen/фон_стена_дерево_3.png'), allow_stretch=True,
                                            keep_ratio=False)

        self.wall_box_level_ten.add_widget(self.climb_wall_level_ten)

        self.coin_box_level_ten_1 = AnchorLayout(padding=(x_level * 1.5, 0, x_level * 2, y * 7))
        self.coin_box_level_ten_2 = AnchorLayout(padding=(x_level * 0.5, -y, x_level * 3, y * 8))
        self.coin_box_level_ten_3 = AnchorLayout(padding=(x_level * 1.5, -y * 2, x_level * 2, y * 9))
        self.coin_box_level_ten_4 = AnchorLayout(padding=(x_level * 1.5, -y * 4, x_level * 2, y * 11))
        self.coin_box_level_ten_5 = AnchorLayout(padding=(x_level * 0.5, -y * 5, x_level * 3, y * 12))
        self.coin_box_level_ten_6 = AnchorLayout(padding=(x_level * 1.5, -y * 6, x_level * 2, y * 13))
        self.coin_box_level_ten_7 = AnchorLayout(padding=(x_level * 1.5, -y * 10, x_level * 2, y * 17))
        self.coin_box_level_ten_8 = AnchorLayout(padding=(x_level * 0.5, -y * 11, x_level * 3, y * 18))
        self.coin_box_level_ten_9 = AnchorLayout(padding=(x_level * 1.5, -y * 12, x_level * 2, y * 19))
        self.coin_box_level_ten_10 = AnchorLayout(padding=(x_level * 1.5, -y * 14, x_level * 2, y * 21))
        self.coin_box_level_ten_11 = AnchorLayout(padding=(x_level * 0.5, -y * 15, x_level * 3, y * 22))
        self.coin_box_level_ten_12 = AnchorLayout(padding=(x_level * 1.5, -y * 16, x_level * 2, y * 23))

        self.coin_boxes_level_ten = [self.coin_box_level_ten_1, self.coin_box_level_ten_2,
                                       self.coin_box_level_ten_3,
                                       self.coin_box_level_ten_4, self.coin_box_level_ten_5,
                                       self.coin_box_level_ten_6,
                                       self.coin_box_level_ten_7, self.coin_box_level_ten_8,
                                       self.coin_box_level_ten_9,
                                       self.coin_box_level_ten_10, self.coin_box_level_ten_11,
                                       self.coin_box_level_ten_12]

        self.coins_level_ten = []

        self.coin_check_level_ten = 0

        for i in range(12):
            i = Widget()
            self.coins_level_ten.append(i)

        for a in self.coin_boxes_level_ten[:]:
            a.add_widget(self.coins_level_ten[self.coin_check_level_ten])
            self.coin_check_level_ten += 1

        self.coin_count_level_ten = 0

        self.knight_image_box_level_ten = BoxLayout(padding=(-x, 0, x / 1.5, 0))

        self.knight_image_jump_level_ten = Widget()
        self.knight_image_end_level_ten = Widget()
        self.knight_image_start_level_ten = Image(source=('Design Screen/a.png'))
        self.knight_image_walk_level_ten = Widget()
        self.knight_image_sit_level_ten = Widget()
        self.knight_image_sit_up_level_ten = Widget()
        self.knight_box_level_ten = BoxLayout(padding=(x * 2.2, y * 4, x * 2.8, y * 3))

        self.frages_box_level_ten_down = BoxLayout(padding=(x * 2, 0, x * 3.5, y * 6))
        self.frages_box_image_level_ten_down = BoxLayout(padding=(x * 2, 0, x * 3.5, y * 6))
        self.frages_box_image_level_ten_down.add_widget(
            Image(source=('Design Screen/стрела.zip'), anim_delay=.1, keep_ratio=False, allow_stretch=True))
        self.frag_level_ten_down = Widget()
        self.frages_box_image_level_ten_down.y = self.knight_box_level_ten.y + y * 64
        self.frages_box_level_ten_down.y = self.knight_box_level_ten.y + y * 64
        self.frages_box_level_ten_down.add_widget(self.frag_level_ten_down)

        self.frag_kick_level_ten = AnchorLayout(padding=(x * 2.8, -y * 3.3, x * 1.4, y * 10))
        self.frag_kicker_level_ten = Image(source=('Design Screen/disk.zip'), anim_delay=.01, keep_ratio=False,
                                             allow_stretch=True)
        self.frag_kicker_true_level_ten = Widget(size_hint=(.5, .5))
        self.frag_kick_level_ten.add_widget(self.frag_kicker_level_ten)
        self.frag_kick_level_ten.add_widget(self.frag_kicker_true_level_ten)

        self.frag_1_kick_level_ten = AnchorLayout(padding=(x * 2.8, -y * 8.3, x * 1.4, y * 15))
        self.frag_1_kicker_level_ten = Image(source=('Design Screen/disk.zip'), anim_delay=.01, keep_ratio=False,
                                               allow_stretch=True)
        self.frag_1_kicker_true_level_ten = Widget(size_hint=(.5, .5))
        self.frag_1_kick_level_ten.add_widget(self.frag_1_kicker_level_ten)
        self.frag_1_kick_level_ten.add_widget(self.frag_1_kicker_true_level_ten)

        self.frag_2_kick_level_ten = AnchorLayout(padding=(x * 2.8, -y * 13.3, x * 1.4, y * 20))
        self.frag_2_kicker_level_ten = Image(source=('Design Screen/disk.zip'), anim_delay=.01, keep_ratio=False,
                                               allow_stretch=True)
        self.frag_2_kicker_true_level_ten = Widget(size_hint=(.5, .5))
        self.frag_2_kick_level_ten.add_widget(self.frag_2_kicker_level_ten)
        self.frag_2_kick_level_ten.add_widget(self.frag_2_kicker_true_level_ten)

        self.word_box_level_ten = BoxLayout(padding=(x_level * 1.5, -y * 13, x_level * 2, y * 20))
        self.word_image_level_ten = Image(source=('Design Screen/буквы/буква D.png'))
        self.word_box_level_ten.add_widget(self.word_image_level_ten)
        self.Knight_box_letter_level_ten = BoxLayout(padding=(x_level * 0.2, y * 0.6, x_level * 2, y * 7))
        self.Knight_image_box_letter_level_ten = Image(source=('Design Screen/буквы/KNIGHT_10_level.png'))
        self.Knight_box_letter_level_ten.add_widget(self.Knight_image_box_letter_level_ten)
        self.Knight_box_letter_level_ten_empty = BoxLayout(padding=(x_level * 0.2, y * 0.6, x_level * 2, y * 7))
        self.knight_box_button_level_ten = Widget()
        self.knight_box_level_ten.add_widget(self.knight_box_button_level_ten)
        self.knight_image_box_level_ten.add_widget(self.knight_image_start_level_ten)
        self.knight_level_ten_complete_box = BoxLayout(padding=(0, -y * 28.5, 0, y * 28))
        self.knight_level_ten_complete_video = Image(source=('Design Screen/end_level_animation_6.zip'),
                                                       anim_delay=0.03, allow_stretch=True,
                                                       keep_ratio=False, anim_loop=1)
        self.knight_level_ten_complete_box.add_widget(self.knight_level_ten_complete_video)
        self.climb_screen_level_ten.add_widget(self.knight_level_ten_complete_box)
        self.climb_screen_level_ten.add_widget(self.wall_box_level_ten)
        self.climb_screen_level_ten.add_widget(self.frages_box_level_ten_down)
        self.climb_screen_level_ten.add_widget(self.frages_box_image_level_ten_down)
        self.climb_screen_level_ten.add_widget(self.frag_kick_level_ten)
        self.climb_screen_level_ten.add_widget(self.frag_1_kick_level_ten)
        self.climb_screen_level_ten.add_widget(self.frag_2_kick_level_ten)
        self.climb_screen_level_ten.add_widget(self.knight_box_level_ten)
        self.climb_screen_level_ten.add_widget(self.knight_image_box_level_ten)
        self.climb_screen_level_ten.add_widget(self.word_box_level_ten)
        for i in self.coin_boxes_level_ten[:]:
            self.climb_screen_level_ten.add_widget(i)
        self.ten_level_screen_child.add_widget(self.sky_box_level_ten)
        self.ten_level_screen_child.add_widget(self.climb_screen_level_ten)
        self.ten_level_screen.add_widget(self.ten_level_screen_child)

        self.swipe_level_ten = Slider(min=-1, max=1, value=0, step=.5, background_width=(0), cursor_size=(0, 0),
                                        on_touch_up=self.on_touch_up, on_touch_move=self.on_touch_move,
                                        on_touch_down=self.on_touch_down)
        self.ten_level.add_widget(self.ten_level_screen)

        "___________________________________________________________________________________________________________"

        #Создаем экран с поражением
        self.game_over_menu = Screen(name = 'Defeat')
        self.game_over_menu_box = BoxLayout(padding=(150, 300, 150, 250))
        self.game_over_image = Image(source=('Design Screen/Game_over.png'))
        self.game_over_menu_box.add_widget(Button(background_color=(0, 0, 0, 0), on_press=self.press_HOME))
        self.game_over_menu.add_widget(self.game_over_image)
        self.game_over_menu.add_widget(self.game_over_menu_box)

        # Создаем экран с победой
        self.win_menu = Screen(name='Win')
        self.win_menu_box = BoxLayout(padding=(x*2, y*4.5, x*2, y*2.5))
        self.win_image = Image(source=('Design Screen/Win_screen.png'))
        self.win_menu_box.add_widget(Button(background_color=(255, 255, 255, 0), on_press=self.press_HOME))
        self.win_menu.add_widget(self.win_image)
        self.win_menu.add_widget(self.win_menu_box)


        self.sm = ScreenManager(transition=FadeTransition())

        #Первый экран
        self.main_screen = Screen(name='first')
        first_screen = RelativeLayout()

        #кнопка персонажа
        character_box = BoxLayout(padding=(0, y*7, x*4, 0))
        character_button = Button(on_press = self.press_ME, background_color=(0, 0, 0, 0))
        character_box.add_widget(character_button)

        # Кнопка Options
        options_box =  BoxLayout(padding=(0, 0, x*5, y*7))
        options_button = Button(on_press=self.press_OPTIONS, background_color=(0, 0, 0, 0))
        options_box.add_widget(options_button)

        #Кнопка выбора уровня
        play_box = BoxLayout(padding=(0, y, 0, y))
        play_button = Button(on_press=self.press_TAP_TO_START, background_color=(0, 0, 0, 0))
        play_box.add_widget(play_button)

        #Кнопка открытия магазина
        shop_box = BoxLayout(padding=(x*4, y*7, 0, 0))
        shop_button = Button(on_press=self.press_SHOP_BUTTON, background_color=(0, 0, 0, 0))
        shop_box.add_widget(shop_button)


        # Добавить кнопки и картинку на первый экран
        first_screen.add_widget(options_box)
        first_screen.add_widget(play_box)
        first_screen.add_widget(character_box)
        first_screen.add_widget(shop_box)
        self.main_screen.add_widget(Image(source=('Design Screen/первый фон.zip'),anim_delay = .1,  allow_stretch=True,
                                          keep_ratio=False))
        self.main_screen.add_widget(Image(source=('Design Screen/First_screen.png'),  allow_stretch = True,
                                                    keep_ratio = False))
        self.main_screen.add_widget(first_screen)

        # Экран персонажа
        self.character_screen = Screen(name='character')


        # Добавить кнопки и картинку на второй экран
        self.character_screen.add_widget(Image(source=('Design Screen/выбор скина 1.png')))
        self.skin_button_box = BoxLayout(padding = (x*4.5, y*3.3, x*0.8, y*3.8))
        self.skin_button_box.add_widget(Button(on_press=self.press_change_skin, background_color=(0, 0, 0, 0)))
        return_back_character = BoxLayout(padding=(0, 0, x * 5, y * 7))
        return_back_character.add_widget(Button(on_press=self.press_RETURN, background_color=(0, 0, 0, .3)))
        self.character_screen.add_widget(return_back_character)
        self.character_screen.add_widget(self.skin_button_box)

        # Экран Options
        options = Screen(name='options')
        # Кнопка возврата на первый экран
        return_first_screen = BoxLayout(padding=(x*0.5, y*0.5, x*4.5, y*6.5))
        return_first_screen.add_widget(Button(on_press=self.press_RETURN, background_color=(0, 0, 0, .5)))

        # Добавить кнопки и картинку на экран опций
        options.add_widget(Image(source=('Design Screen/Options_screen.png')))
        options.add_widget(return_first_screen)

        """Изоражение 1 скина"""
        self.first_skin = Screen(name='first_skin')
        self.first_skin.add_widget(Image(source=('Design Screen/1 скин.png')))

        """Изоражение 2 скина"""
        self.second_skin = Screen(name='second_skin')
        self.second_skin.add_widget(Image(source=('Design Screen/2 скин.png')))

        """Изоражение 3 скина"""
        self.third_skin = Screen(name='three_skin')
        self.third_skin.add_widget(Image(source=('Design Screen/1 скин.png')))

        """Изоражение 4 скина"""
        self.fourth_skin = Screen(name='four_skin')
        self.fourth_skin.add_widget(Image(source=('Design Screen/2 скин.png')))


        #экран c меню персонажа
        self.skin_screen = Screen(name='skin')
        self.skin_screen.add_widget(Image(source=('Design Screen/выбор скина 1.png')))
        self.screen_box = BoxLayout(padding = (x*0.5, y*1.5, x, y*2))

        self.screen_for_skins = ScreenManager()

        self.screen_for_skins.add_widget(self.first_skin)
        self.screen_for_skins.add_widget(self.second_skin)
        self.screen_for_skins.add_widget(self.third_skin)
        self.screen_for_skins.add_widget(self.fourth_skin)

        self.count_skin = 0
        self.one_skin = True
        self.two_skin = False
        self.three_skin = False
        self.four_skin = False

        self.skins = [self.one_skin, self.two_skin, self.three_skin, self.four_skin]

        self.skin_screen_boxes = BoxLayout(padding = (x*3.2, y*6.5, x*0.8, y))
        self.skin_screen_boxes.add_widget(Button(on_press=self.press_change_skin_for_game,  background_color=(0, 0, 0, 0)))

        self.screen_box.add_widget(self.screen_for_skins)
        self.character_screen.add_widget(self.screen_box)
        self.character_screen.add_widget(self.skin_screen_boxes)

        # Экран с выбором уровня
        self.menu_select_level_screen = Screen(name='Menu_select_level')
        self.intro_image = Image(source = ('Design Screen/introduce.zip'), anim_delay= -1, allow_stretch=True,
                                keep_ratio=False,
                                keep_data=False)

        self.menu_select_level_screen.add_widget(self.intro_image)
        self.play_game = BoxLayout()
        self.play_game.add_widget(Button(background_color=(0, 0, 0, 0), on_press=(self.start_level)))

        self.menu_select_level_screen.add_widget(self.play_game)

        # Присваивание значений для анимации кнопок
        #Экран магазина
        self.items_screen = Screen(name=('items'))
        self.items_screen.add_widget(Image(source=('Design Screen/Items_screen.png')))
        return_back_shop = BoxLayout(padding=(0, 0, x*5, y*7))
        return_back_shop.add_widget(Button(on_press=self.press_RETURN, background_color=(0, 0, 0, .5)))
        items_select_shop_box = BoxLayout(padding = (x, y*7, x, 0))
        items_select_shop_box.add_widget(Button(on_press=self.press_SHUES, background_color=(0, 0, 0, .5)))
        items_select_shop_box.add_widget(Button(on_press=self.press_CLOTHES, background_color=(0, 0, 0, .5)))
        items_select_shop_box.add_widget(Button(on_press=self.press_UPGRADES, background_color=(0, 0, 0, .5)))
        items_select_shop_box.add_widget(Button(on_press=self.press_STORE, background_color=(0, 0, 0, .5)))
        self.items_screen.add_widget(return_back_shop)
        self.items_screen.add_widget(items_select_shop_box)

        #экран обуви
        self.shues_screen = Screen(name=('shues'))
        self.shues_screen.add_widget(Image(source=('Design Screen/Shues_screen.png')))
        return_back_shues = BoxLayout(padding=(0, 0, x * 5, y * 7))
        return_back_shues.add_widget(Button(on_press=self.press_RETURN_TO_ITEMS, background_color=(0, 0, 0, .5)))
        shues_select_shop_box = BoxLayout(padding=(x, y * 7, x, 0))
        shues_select_shop_box.add_widget(Button(on_press=self.press_SHUES, background_color=(0, 0, 0, .5)))
        shues_select_shop_box.add_widget(Button(on_press=self.press_CLOTHES, background_color=(0, 0, 0, .5)))
        shues_select_shop_box.add_widget(Button(on_press=self.press_UPGRADES, background_color=(0, 0, 0, .5)))
        shues_select_shop_box.add_widget(Button(on_press=self.press_STORE, background_color=(0, 0, 0, .5)))
        self.shues_screen.add_widget(return_back_shues)
        self.shues_screen.add_widget(shues_select_shop_box)

        #экран одежды
        self.clothes_screen = Screen(name=('clothes'))
        self.clothes_screen.add_widget(Image(source=('Design Screen/Clothes_screen.png')))
        return_back_clothes = BoxLayout(padding=(0, 0, x * 5, y * 7))
        return_back_clothes.add_widget(Button(on_press=self.press_RETURN_TO_ITEMS, background_color=(0, 0, 0, .5)))
        clothes_select_shop_box = BoxLayout(padding=(x, y * 7, x, 0))
        clothes_select_shop_box.add_widget(Button(on_press=self.press_SHUES, background_color=(0, 0, 0, .5)))
        clothes_select_shop_box.add_widget(Button(on_press=self.press_CLOTHES, background_color=(0, 0, 0, .5)))
        clothes_select_shop_box.add_widget(Button(on_press=self.press_UPGRADES, background_color=(0, 0, 0, .5)))
        clothes_select_shop_box.add_widget(Button(on_press=self.press_STORE, background_color=(0, 0, 0, .5)))
        self.clothes_screen.add_widget(return_back_clothes)
        self.clothes_screen.add_widget(clothes_select_shop_box)

        #экран улучшений
        self.upgrades_screen = Screen(name=('upgrades'))
        self.upgrades_screen.add_widget(Image(source=('Design Screen/Upgrade_screen.png')))
        return_back_upgrades = BoxLayout(padding=(0, 0, x * 5, y * 7))
        return_back_upgrades.add_widget(Button(on_press=self.press_RETURN_TO_ITEMS, background_color=(0, 0, 0, .5)))
        upgrades_select_shop_box = BoxLayout(padding=(x, y * 7, x, 0))
        upgrades_select_shop_box.add_widget(Button(on_press=self.press_SHUES, background_color=(0, 0, 0, .5)))
        upgrades_select_shop_box.add_widget(Button(on_press=self.press_CLOTHES, background_color=(0, 0, 0, .5)))
        upgrades_select_shop_box.add_widget(Button(on_press=self.press_UPGRADES, background_color=(0, 0, 0, .5)))
        upgrades_select_shop_box.add_widget(Button(on_press=self.press_STORE, background_color=(0, 0, 0, .5)))
        self.upgrades_screen.add_widget(return_back_upgrades)
        self.upgrades_screen.add_widget(upgrades_select_shop_box)

        #магазин
        self.store_screen = Screen(name=('store'))
        self.store_screen.add_widget(Image(source=('Design Screen/Store_screen.png')))
        store_back_upgrades = BoxLayout(padding=(0, 0, x * 5, y * 7))
        store_back_upgrades.add_widget(Button(on_press=self.press_RETURN_TO_ITEMS, background_color=(0, 0, 0, .5)))
        store_select_shop_box = BoxLayout(padding=(x, y * 7, x, 0))
        store_select_shop_box.add_widget(Button(on_press=self.press_SHUES, background_color=(0, 0, 0, .5)))
        store_select_shop_box.add_widget(Button(on_press=self.press_CLOTHES, background_color=(0, 0, 0, .5)))
        store_select_shop_box.add_widget(Button(on_press=self.press_UPGRADES, background_color=(0, 0, 0, .5)))
        store_select_shop_box.add_widget(Button(on_press=self.press_STORE, background_color=(0, 0, 0, .5)))
        self.store_screen.add_widget(store_back_upgrades)
        self.store_screen.add_widget(store_select_shop_box)

        #Добавляем экраны к ScreenManager
        self.sm.add_widget(self.main_screen)
        self.sm.add_widget(self.character_screen)
        self.sm.add_widget(self.skin_screen)
        self.sm.add_widget(self.items_screen)

        self.sm.add_widget(self.shues_screen)
        self.sm.add_widget(self.clothes_screen)
        self.sm.add_widget(self.upgrades_screen)
        self.sm.add_widget(self.store_screen)

        self.sm.add_widget(options)
        self.sm.add_widget(self.menu_select_level_screen)
        """self.sm.add_widget(self.america_screen)"""
        self.sm.add_widget(self.first_level)
        self.sm.add_widget(self.second_level)
        self.sm.add_widget(self.three_level)
        self.sm.add_widget(self.four_level)
        self.sm.add_widget(self.five_level)
        self.sm.add_widget(self.six_level)
        self.sm.add_widget(self.seven_level)
        self.sm.add_widget(self.eight_level)
        self.sm.add_widget(self.nine_level)
        self.sm.add_widget(self.ten_level)
        self.sm.add_widget(self.game_over_menu)
        self.sm.add_widget(self.win_menu)
        self.sm.add_widget(self.maps_image_screen)

        self.count_screen = [ self.main_screen, self.game_over_menu,
                             self.win_menu,  self.character_screen, self.skin_screen,
                             self.items_screen, self.first_level]

        self.levels = [self.first_level, self.second_level, self.three_level, self.four_level, self.five_level, self.six_level, self.seven_level,
                       self.eight_level, self.nine_level, self.ten_level]
        self.level_screen = [self.first_level_screen, self.second_level_screen, self.three_level_screen, self.four_level_screen,
                             self.five_level_screen, self.six_level_screen, self.seven_level_screen, self.eight_level_screen,
                             self.nine_level_screen, self.ten_level_screen]
        self.level_screen_child = [self.first_level_screen_child, self.second_level_screen_child, self.three_level_screen_child,
                                   self.four_level_screen_child, self.five_level_screen_child, self.six_level_screen_child,
                                   self.seven_level_screen_child, self.eight_level_screen_child, self.nine_level_screen_child,
                                   self.ten_level_screen_child]
        self.knight_image_boxes = [self.knight_image_box_level_one, self.knight_image_box_level_two, self.knight_image_box_level_three,
                                   self.knight_image_box_level_four, self.knight_image_box_level_five, self.knight_image_box_level_six,
                                   self.knight_image_box_level_seven, self.knight_image_box_level_eight, self.knight_image_box_level_nine,
                                   self.knight_image_box_level_ten]
        self.knight_box = [self.knight_box_level_one, self.knight_box_level_two, self.knight_box_level_three, self.knight_box_level_four,
                           self.knight_box_level_five, self.knight_box_level_six, self.knight_box_level_seven, self.knight_box_level_eight,
                           self.knight_box_level_nine, self.knight_box_level_ten]
        self.knight_image_start = [self.knight_image_start_level_one, self.knight_image_start_level_two, self.knight_image_start_level_three,
                                   self.knight_image_start_level_four, self.knight_image_start_level_five, self.knight_image_start_level_six,
                                   self.knight_image_start_level_seven, self.knight_image_start_level_eight, self.knight_image_start_level_nine,
                                   self.knight_image_start_level_ten]
        self.knight_image_walk = [self.knight_image_walk_level_one, self.knight_image_walk_level_two, self.knight_image_walk_level_three,
                                  self.knight_image_walk_level_four, self.knight_image_walk_level_five, self.knight_image_walk_level_six,
                                  self.knight_image_walk_level_seven, self.knight_image_walk_level_eight, self.knight_image_walk_level_nine,
                                  self.knight_image_walk_level_ten]
        self.knight_image_jump = [self.knight_image_jump_level_one, self.knight_image_jump_level_two, self.knight_image_jump_level_three,
                                  self.knight_image_jump_level_four, self.knight_image_jump_level_five, self.knight_image_jump_level_six,
                                  self.knight_image_jump_level_seven, self.knight_image_jump_level_eight, self.knight_image_jump_level_nine,
                                  self.knight_image_jump_level_ten]
        self.knight_image_end = [self.knight_image_end_level_one, self.knight_image_end_level_two, self.knight_image_end_level_three,
                                 self.knight_image_end_level_four, self.knight_image_end_level_five, self.knight_image_end_level_six,
                                 self.knight_image_end_level_seven, self.knight_image_end_level_eight, self.knight_image_end_level_nine,
                                 self.knight_image_end_level_ten]
        self.knight_image_sit = [self.knight_image_sit_level_one, self.knight_image_sit_level_two, self.knight_image_sit_level_three,
                                 self.knight_image_sit_level_four, self.knight_image_sit_level_five, self.knight_image_sit_level_six,
                                 self.knight_image_sit_level_seven, self.knight_image_sit_level_eight, self.knight_image_sit_level_nine,
                                 self.knight_image_sit_level_ten]
        self.knight_image_sit_up = [self.knight_image_sit_up_level_one, self.knight_image_sit_up_level_two,
                                 self.knight_image_sit_up_level_three, self.knight_image_sit_up_level_four,
                                 self.knight_image_sit_up_level_five, self.knight_image_sit_up_level_six, self.knight_image_sit_up_level_seven,
                                    self.knight_image_sit_up_level_eight, self.knight_image_sit_up_level_nine, self.knight_image_sit_up_level_ten]
        self.knight_box_button = [self.knight_box_button_level_one, self.knight_box_button_level_two, self.knight_box_button_level_three,
                                  self.knight_box_button_level_four , self.knight_box_button_level_five, self.knight_box_button_level_six,
                                  self.knight_box_button_level_seven, self.knight_box_button_level_eight, self.knight_box_button_level_nine,
                                  self.knight_box_button_level_ten]
        self.climb_screen = [self.climb_screen_level_one, self.climb_screen_level_two, self.climb_screen_level_three,
                             self.climb_screen_level_four, self.climb_screen_level_five,self.climb_screen_level_six ,
                             self.climb_screen_level_seven, self.climb_screen_level_eight, self.climb_screen_level_nine,
                             self.climb_screen_level_ten]


        self.sky_box = [self.sky_box_level_one, self.sky_box_level_two, self.sky_box_level_three, self.sky_box_level_four,
                        self.sky_box_level_five, self.sky_box_level_six, self.sky_box_level_seven, self.sky_box_level_eight,
                        self.sky_box_level_nine, self.sky_box_level_ten]

        self.coin_check = [self.coin_check_level_one, self.coin_check_level_two, self.coin_check_level_three,
                           self.coin_check_level_four, self.coin_check_level_five, self.coin_check_level_six,
                           self.coin_check_level_seven, self.coin_check_level_eight, self.coin_check_level_nine,
                           self.coin_check_level_ten]
        self.coins = [self.coins_level_one, self.coins_level_two, self.coins_level_three, self.coins_level_four,
                      self.coins_level_five, self.coins_level_six, self.coins_level_seven,  self.coins_level_eight,
                      self.coins_level_nine,   self.coins_level_ten]
        self.coin_boxes = [self.coin_boxes_level_one, self.coin_boxes_level_two, self.coin_boxes_level_three ,
                           self.coin_boxes_level_four, self.coin_boxes_level_five, self.coin_boxes_level_six,
                           self.coin_boxes_level_seven, self.coin_boxes_level_eight, self.coin_boxes_level_nine,
                           self.coin_boxes_level_ten]

        self.wall_box = [self.wall_box_level_one, self.wall_box_level_two, self.wall_box_level_three,
                         self.wall_box_level_four, self.wall_box_level_five, self.wall_box_level_six,
                         self.wall_box_level_seven, self.wall_box_level_eight, self.wall_box_level_nine,
                         self.wall_box_level_ten]
        self.maps_button_box = [self.maps_button_box_level_one, self.maps_button_box_level_two,
                                self.maps_button_box_level_three, self.maps_button_box_level_four,
                                self.maps_button_box_level_five, self.maps_button_box_level_six,
                                self.maps_button_box_level_seven, self.maps_button_box_level_eight,
                                self.maps_button_box_level_nine, self.maps_button_box_level_ten]

        self.frags_level_one = [self.frag_level_one, self.frag_1_level_one, self.frag_2_level_one]
        self.frags_image_level_one = [self.frages_box_image_level_one, self.frages_box_image_1_level_one,
                                      self.frages_box_image_2_level_one]

        self.frags_level_two_down = [self.frag_level_two_down, self.frag_1_level_two_down, self.frag_2_level_two_down]
        self.frags_box_level_two_down = [self.frages_box_level_two_down, self.frages_box_1_level_two_down,
                                         self.frages_box_2_level_two_down]
        self.frags_image_level_two_down = [self.frages_box_image_level_two_down, self.frages_box_image_1_level_two_down,
                                           self.frages_box_image_2_level_two_down]

        self.frags_level_three_down = [self.frag_level_three_down]
        self.frags_box_level_three_down = [self.frages_box_level_three_down]
        self.frags_image_level_three_down = [self.frages_box_image_level_three_down]
        self.frags_image_level_three = [self.frages_box_image_level_three, self.frages_box_image_1_level_three]
        self.frags_level_three = [self.frag_level_three, self.frag_1_level_three]

        self.frags_level_four_down = [self.frag_level_four_down]
        self.frags_box_level_four_down = [self.frages_box_level_four_down]
        self.frags_image_level_four_down = [self.frages_box_image_level_four_down]
        self.frags_image_level_four = [self.frages_box_image_level_four]
        self.frags_level_four = [self.frag_level_four, self.but_text]

        self.frags_level_five_down = [self.frag_level_five_down]
        self.frags_box_level_five_down = [self.frages_box_level_five_down]
        self.frags_image_level_five_down = [self.frages_box_image_level_five_down]
        self.frags_image_level_five = [self.frages_box_image_level_five]
        self.frags_level_five = [self.frag_level_five, self.frag_kicker_true_level_five]

        self.frags_level_six_down = [self.frag_level_six_down]
        self.frags_box_level_six_down = [self.frages_box_level_six_down]
        self.frags_image_level_six_down = [self.frages_box_image_level_six_down]
        self.frags_level_six = [self.frag_kicker_true_level_six, self.frag_1_kicker_true_level_six, self.frag_2_kicker_true_level_six]

        self.frags_level_seven_down = [self.frag_level_seven_down]
        self.frags_box_level_seven_down = [self.frages_box_level_seven_down]
        self.frags_image_level_seven_down = [self.frages_box_image_level_seven_down]
        self.frags_level_seven = [self.frag_kicker_true_level_seven, self.frag_1_kicker_true_level_seven,
                                self.frag_2_kicker_true_level_seven]

        self.frags_level_eight_down = [self.frag_level_eight_down]
        self.frags_box_level_eight_down = [self.frages_box_level_eight_down]
        self.frags_image_level_eight_down = [self.frages_box_image_level_eight_down]
        self.frags_level_eight = [self.frag_kicker_true_level_eight, self.frag_1_kicker_true_level_eight,
                                  self.frag_2_kicker_true_level_eight]

        self.frags_level_nine_down = [self.frag_level_nine_down]
        self.frags_box_level_nine_down = [self.frages_box_level_nine_down]
        self.frags_image_level_nine_down = [self.frages_box_image_level_nine_down]
        self.frags_level_nine = [self.frag_kicker_true_level_nine, self.frag_1_kicker_true_level_nine,
                                  self.frag_2_kicker_true_level_nine]

        self.frags_level_ten_down = [self.frag_level_ten_down]
        self.frags_box_level_ten_down = [self.frages_box_level_ten_down]
        self.frags_image_level_ten_down = [self.frages_box_image_level_ten_down]
        self.frags_level_ten = [self.frag_kicker_true_level_ten, self.frag_1_kicker_true_level_ten,
                                  self.frag_2_kicker_true_level_ten]


        self.frags = [self.frags_level_one, self.frags_level_three, self.frags_level_four, self.frags_level_five,
                      self.frags_level_six, self.frags_level_seven, self.frags_level_eight, self.frags_level_nine,
                      self.frags_level_ten]
        self.frags_down = [self.frags_level_two_down, self.frags_level_three_down, self.frags_level_four_down,
                           self.frags_level_five_down, self.frags_level_six_down, self.frags_level_seven_down,
                           self.frags_level_eight_down, self.frags_level_nine_down, self.frags_level_ten_down]
        self.frags_image_down = [self.frags_image_level_two_down, self.frags_image_level_three_down, self.frags_image_level_four_down,
                                 self.frags_image_level_five_down, self.frags_image_level_six_down, self.frags_image_level_seven_down,
                                 self.frags_image_level_eight_down, self.frags_image_level_nine_down, self.frags_image_level_ten_down]
        self.frags_image_static = [self.frags_image_level_one, self.frags_image_level_three, self.frags_image_level_four,
                                   self.frags_image_level_five, None]
        self.frags_box_down = [self.frags_box_level_two_down, self.frags_box_level_three_down, self.frags_box_level_four_down,
                               self.frags_box_level_five_down, self.frags_box_level_six_down, self.frags_box_level_seven_down,
                               self.frags_box_level_eight_down, self.frags_box_level_nine_down, self.frags_box_level_ten_down]

        self.swipe = [self.swipe_level_one,self.swipe_level_two, self.swipe_level_three, self.swipe_level_four,
                      self.swipe_level_five, self.swipe_level_six, self.swipe_level_seven, self.swipe_level_eight,
                      self.swipe_level_nine, self.swipe_level_ten]

        self.level_complete = [self.first_level_complete, self.second_level_complete, self.three_level_complete,
                               self.four_level_complete, self.five_level_complete, self.six_level_complete, self.seven_level_complete,
                               self.eight_level_complete, self.nine_level_complete, self.ten_level_complete]

        self.level_start  = [self.first_level_start, self.second_level_start, self.three_level_start, self.four_level_start,
                             self.five_level_start, self.six_level_start, self.seven_level_start, self.eight_level_start,
                             self.nine_level_start, self.ten_level_start]

        self.words_knight = [self.word_image_level_one, self.word_image_level_two, self.word_image_level_three,
                             self.word_image_level_four, self.word_image_level_five, self.word_image_level_six,
                             self.word_image_level_seven, self.word_image_level_eight, self.word_image_level_nine,
                             self.word_image_level_ten]

        self.Knight_letter = [self.Knight_box_letter_level_one, self.Knight_box_letter_level_two,
                              self.Knight_box_letter_level_three, self.Knight_box_letter_level_four,
                              self.Knight_box_letter_level_five, self.Knight_box_letter_level_six]

        self.Lord_letter = [self.Knight_box_letter_level_seven, self.Knight_box_letter_level_eight,
                            self.Knight_box_letter_level_nine, self.Knight_box_letter_level_ten]

        self.Knight_letter_images = [self.Knight_image_box_letter_level_one, self.Knight_image_box_letter_level_two,
                                     self.Knight_image_box_letter_level_three,
                                     self.Knight_image_box_letter_level_four, self.Knight_image_box_letter_level_five,
                                     self.Knight_image_box_letter_level_six]

        self.Lord_letter_images = [self.Knight_image_box_letter_level_seven, self.Knight_image_box_letter_level_eight,
                                   self.Knight_image_box_letter_level_nine, self.Knight_image_box_letter_level_ten]

        self.Knight_box_letter_empty = [self.Knight_box_letter_level_one_empty, self.Knight_box_letter_level_two_empty,
                                        self.Knight_box_letter_level_three_empty, self.Knight_box_letter_level_four_empty,
                                        self.Knight_box_letter_level_five_empty, self.Knight_box_letter_level_six_empty]

        self.Lord_box_letter_empty = [self.Knight_box_letter_level_seven_empty, self.Knight_box_letter_level_eight_empty,
                                      self.Knight_box_letter_level_nine_empty, self.Knight_box_letter_level_ten_empty]

        self.word_flags = [self.K_collect, self.N_collect, self.I_collect, self.G_collect, self.H_collect, self.T_collect]

        self.word_flags_lord = [self.L_collect, self.O_collect, self.R_collect, self.D_collect]

        self.end_level_movie = [self.end_level_movie_level_one, self.end_level_movie_level_two, self.end_level_movie_level_three,
                                self.end_level_movie_level_four, self.end_level_movie_level_five, self.end_level_movie_level_six,
                                self.end_level_movie_level_seven, self.end_level_movie_level_eight, self.end_level_movie_level_nine,
                                self.end_level_movie_level_ten]

        self.maps_button_box_rel_coin_boxes = [self.maps_button_box_level_one_rel_coin_box, self.maps_button_box_level_two_rel_coin_box,
                                               self.maps_button_box_level_three_rel_coin_box, self.maps_button_box_level_four_rel_coin_box,
                                               self.maps_button_box_level_five_rel_coin_box,self.maps_button_box_level_six_rel_coin_box,
                                               self.maps_button_box_level_seven_rel_coin_box, self.maps_button_box_level_eight_rel_coin_box,
                                               self.maps_button_box_level_nine_rel_coin_box, self.maps_button_box_level_ten_rel_coin_box]

        self.maps_image = [ self.maps_image_level_one,  self.maps_image_level_two,  self.maps_image_level_three, self.maps_image_level_four,
                            self.maps_image_level_five, self.maps_image_level_six, self.maps_image_level_seven, self.maps_image_level_eight,
                            self.maps_image_level_nine, self.maps_image_level_ten]

        self.maps_shadow_image = [self.maps_image_shadow_box_level_one, self.maps_image_shadow_box_level_two, self.maps_image_shadow_box_level_three,
                                  self.maps_image_shadow_box_level_four, self.maps_image_shadow_box_level_five, self.maps_image_shadow_box_level_six,
                                  self.maps_image_shadow_box_level_seven, self.maps_image_shadow_box_level_eight, self.maps_image_shadow_box_level_nine,
                                  self.maps_image_shadow_box_level_ten]

        self.maps_button_box_rel_letter_boxes = [self.maps_button_box_rel_letter_boxes_level_one, self.maps_button_box_rel_letter_boxes_level_two,
                                                 self.maps_button_box_rel_letter_boxes_level_three, self.maps_button_box_rel_letter_boxes_level_four,
                                                 self.maps_button_box_rel_letter_boxes_level_five, self.maps_button_box_rel_letter_boxes_level_six,
                                                 self.maps_button_box_rel_letter_boxes_level_seven, self.maps_button_box_rel_letter_boxes_level_eight,
                                                 self.maps_button_box_rel_letter_boxes_level_nine, self.maps_button_box_rel_letter_boxes_level_ten]

        self.maps_button_box_levels_rel = [self.maps_button_box_level_one_rel, self.maps_button_box_level_two_rel, self.maps_button_box_level_three_rel,
                                           self.maps_button_box_level_four_rel, self.maps_button_box_level_five_rel, self.maps_button_box_level_six_rel,
                                           self.maps_button_box_level_seven_rel, self.maps_button_box_level_eight_rel, self.maps_button_box_level_nine_rel,
                                           self.maps_button_box_level_ten_rel]

        self.level_try = [self.level_try_level_one, self.level_try_level_two, self.level_try_level_three, self.level_try_level_four, self.level_try_level_five,
                          self.level_try_level_six, self.level_try_level_seven, self.level_try_level_eight, self.level_try_level_nine,
                          self.level_try_level_ten]

        self.frag_kick_image = [self.frag_kick_level_five, self.frag_kick_level_six, self.frag_2_kick_level_six,
                                self.frag_kick_level_seven, self.frag_2_kick_level_seven, self.frag_kick_level_eight, self.frag_2_kick_level_eight,
                                self.frag_kick_level_nine, self.frag_2_kick_level_nine, self.frag_kick_level_ten, self.frag_2_kick_level_ten]

        self.button_boxes = [self.button_box_level_one, self.button_box_level_two, self.button_box_level_three,
                             self.button_box_level_four, self.button_box_level_five, self.button_box_level_six,
                             self.button_box_level_seven, self.button_box_level_eight, self.button_box_level_nine,
                             self.button_box_level_ten]

        self.stars_box = [self.stars_box_level_one, self.stars_box_level_two, self.stars_box_level_three,
                          self.stars_box_level_four, self.stars_box_level_five, self.stars_box_level_six,
                          self.stars_box_level_seven, self.stars_box_level_eight, self.stars_box_level_nine,
                          self.stars_box_level_ten]

        print('зщз')
        self.stars = [self.one_stars, self.two_stars, self.three_stars]

        self.level_count = 4




        return self.sm



if __name__ == '__main__':
    Climbing().run()