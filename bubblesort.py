from tkinter import Button
from tkinter import Tk
from tkinter import DISABLED 
from graphics import Rectangle
import random
import time

class BubbleSort():
    def __init__(self, window):
        self.__window = window
        self.__win_root = window.get_root()
        self.__win_canvas = window.get_canvas()

        self.__btn_play_pause = None
        self.__btn_next_outer_iter = None
        self.__btn_next_inner_iter = None
        self.__btn_prev_outer_state = None
        self.__btn_prev_inner_state = None
        self.__btn_speed_plus = None
        self.__btn_speed_min = None
        self.__btn_reset = None

        self.__reset()




    def __reset(self):
        self.__pause = True
        self.is_sorted = False
        self.__win_canvas.delete("all")
        # TODO:this should be improved
        self.list = []
        width = 10
        self.max_len = self.__window.get_width() // width;

        for i in range(self.max_len, 0, -1):
            self.list.append((i, "white"))
        random.shuffle(self.list)
        print("len of list: ", len(self.list))
        self.recwidth = 10
        # spacing = 10
        max_len = self.__window.get_width() // self.recwidth;

        self.recs = []
        self.__fill_rectangles()
        self.__draw_initial_rectangles()

        self.pause = True
        self.inner_index = 1
        self.speed = 0.1
        self.start_x_btn = 20


    def draw(self):
        # draw buttons
        self.__draw_play_pause_btn()
        self.__draw_next_outer_iter_btn()
        self.__draw_prev_outer_state_btn()
        self.__draw_next_inner_iter_btn()
        self.__draw_prev_inner_state_btn()
        self.__draw_speed_plus_btn()
        self.__draw_speed_min_btn()
        self.__draw_reset_btn()
        # draw information
        # draw initial rectangles
        pass

    def draw_rectangle(self, index, color):
        if self.is_sorted:
            color = "green"
        self.recs[index].draw(self.__win_canvas, color=color);
    
    def draw_rectangles(self):
        self.__win_canvas.delete("all")

        x0 = 0
        for rec in self.recs:
            rec.draw(self.__win_canvas, x0)
            x0 += self.recwidth


    def __fill_rectangles(self):
        startx  = 0
        for num, color in self.list:
            self.recs.append(
                    Rectangle(startx, 
                              self.__window.get_height(),
                              self.recwidth, 
                              self.__window.get_height(),
                              color, 
                              num, 
                              self.max_len));
            startx += self.recwidth

    def __draw_initial_rectangles(self):
        for i in range(0, len(self.recs)):
            self.draw_rectangle(i, "white")

    def __draw_play_pause_btn(self):
        self.__btn_play_pause = Button(self.__win_root, 
                     text="play/pause", 
                     command=self.__handle_play_pause)
        self.__btn_play_pause.place(x = self.start_x_btn, y = 0)
        self.__window.redraw()
    
    def __draw_next_outer_iter_btn(self):
        self.__btn_next_outer_iter = Button(self.__win_root, 
                     text="next outer iteration", 
                     command=self.__handle_next_outer_iter)
        btn1_width = self.__btn_play_pause.winfo_width()
        curr_btn_width = self.__btn_next_outer_iter.winfo_width()
        self.__btn_next_outer_iter.place(
                x = self.start_x_btn + btn1_width + curr_btn_width,
                y = 0)
        self.__window.redraw()

    def __draw_prev_outer_state_btn(self):
        self.__btn_prev_outer_state = Button(self.__win_root, 
                     text="prev outer state", 
                     command=None)
        btn1_width = self.__btn_play_pause.winfo_width()
        btn2_width = self.__btn_next_outer_iter.winfo_width()
        curr_btn_width = self.__btn_prev_outer_state.winfo_width()
        self.__btn_prev_outer_state.place(
                x = self.start_x_btn + btn1_width + btn2_width + curr_btn_width,
                y = 0)
        # TODO: implement handler and remove this
        self.__btn_prev_outer_state.config(state=DISABLED)
        self.__window.redraw()
    
    def __draw_next_inner_iter_btn(self):
        self.__btn_next_inner_iter = Button(self.__win_root, 
                     text="next inner iteration", 
                     command=self.__handle_next_inner_iter)
        btn1_width = self.__btn_play_pause.winfo_width()
        btn2_width = self.__btn_next_outer_iter.winfo_width()
        btn3_width  = self.__btn_prev_outer_state.winfo_width()
        curr_btn_width = self.__btn_next_inner_iter.winfo_width()
        self.__btn_next_inner_iter.place(
                x = self.start_x_btn + btn1_width + btn2_width + btn3_width + curr_btn_width,
                y = 0)
        self.__window.redraw()

    def __draw_prev_inner_state_btn(self):
        self.__btn_prev_inner_state = Button(self.__win_root, 
                     text="prev inner state", 
                     command=None)
        btn1_width = self.__btn_play_pause.winfo_width()
        btn2_width = self.__btn_next_outer_iter.winfo_width()
        btn3_width  = self.__btn_prev_outer_state.winfo_width()
        btn4_width  = self.__btn_next_inner_iter.winfo_width()
        curr_btn_width = self.__btn_prev_inner_state.winfo_width()
        prev_btn_widths = btn1_width + btn2_width + btn3_width + btn4_width 
        self.__btn_prev_inner_state.place(
                x = self.start_x_btn + prev_btn_widths + curr_btn_width,
                y = 0)
        # TODO: implement handler and remove this
        self.__btn_prev_inner_state.config(state=DISABLED)
        self.__window.redraw()
    
    def __draw_speed_plus_btn(self):
        self.__btn_speed_plus = Button(self.__win_root, 
                     text="speed++", 
                     command=self.__handle_speed_plus)
        btn1_width = self.__btn_play_pause.winfo_width()
        btn2_width = self.__btn_next_outer_iter.winfo_width()
        btn3_width = self.__btn_prev_outer_state.winfo_width()
        btn4_width = self.__btn_next_inner_iter.winfo_width()
        btn5_width = self.__btn_prev_inner_state.winfo_width()
        prev_btn_widths = btn1_width + btn2_width + btn3_width + btn4_width + btn5_width
        curr_btn_width = self.__btn_speed_plus.winfo_width()
        self.__btn_speed_plus.place(
                x = self.start_x_btn + prev_btn_widths + curr_btn_width,
                y = 0)
        self.__window.redraw()
    
    def __draw_speed_min_btn(self):
        self.__btn_speed_min = Button(self.__win_root, 
                     text="speed--", 
                     command=self.__handle_speed_min)
        btn1_width = self.__btn_play_pause.winfo_width()
        btn2_width = self.__btn_next_outer_iter.winfo_width()
        btn3_width = self.__btn_prev_outer_state.winfo_width()
        btn4_width = self.__btn_next_inner_iter.winfo_width()
        btn5_width = self.__btn_prev_inner_state.winfo_width()
        btn6_width = self.__btn_speed_plus.winfo_width()
        prev_btn_widths = btn1_width + btn2_width + btn3_width + btn4_width + btn5_width+ btn6_width
        curr_btn_width = self.__btn_speed_min.winfo_width()
        self.__btn_speed_min.place(
                x = self.start_x_btn + prev_btn_widths + curr_btn_width,
                y = 0)
        self.__window.redraw()
    
    def __draw_reset_btn(self):
        self.__btn_reset = Button(self.__win_root, 
                     text="reset", 
                     command=self.__reset)
        btn1_width = self.__btn_play_pause.winfo_width()
        btn2_width = self.__btn_next_outer_iter.winfo_width()
        btn3_width = self.__btn_prev_outer_state.winfo_width()
        btn4_width = self.__btn_next_inner_iter.winfo_width()
        btn5_width = self.__btn_prev_inner_state.winfo_width()
        btn6_width = self.__btn_speed_plus.winfo_width()
        btn7_width  = self.__btn_speed_min.winfo_width()
        prev_btn_widths = btn1_width + btn2_width + btn3_width + btn4_width + btn5_width+ btn6_width + btn7_width
        curr_btn_width = self.__btn_reset.winfo_width()
        self.__btn_reset.place(
                x = self.start_x_btn + prev_btn_widths + curr_btn_width,
                y = 0)
        self.__window.redraw()

    def __handle_speed_plus(self):
        self.speed *= 0.1

    def __handle_speed_min(self):
        self.speed /= 0.1

    def __handle_play_pause(self):
        self.pause = not self.pause

        # outer loop
        while self.is_sorted == False:
            print("outer loop:", self.is_sorted)
            if self.pause == True:
                print("break: self.pause is true")
                break
            self.__play_pause()

    def __play_pause(self):
        self.is_sorted = True
        if self.inner_index + 1 == len(self.recs):
            self.inner_index = 1
        for i in range(self.inner_index, len(self.recs)):
            if self.pause == True:
                print("stopping inner iteration: self.pause is true")
                return
            self.__handle_next_inner_iter()

    def __color_considered_rectangles(self, i):
        if i > 1:
            self.draw_rectangle(i - 2, "white")
            self.draw_rectangle(i - 1, "red")
            self.draw_rectangle(i, "red")
            self.__window.redraw()

    def __swap_if_greater(self, i):
            time.sleep(self.speed)
            if self.recs[i - 1].value > self.recs[i].value:
                self.recs[i - 1], self.recs[i] = self.recs[i], self.recs[i - 1],
                self.draw_rectangles()
                self.is_sorted = False

    def __handle_next_outer_iter(self):
        self.is_sorted = True
        if self.inner_index + 1 == len(self.recs):
            self.inner_index = 1
        for i in range(self.inner_index, len(self.recs)):
            self.__handle_next_inner_iter()
    
    def __handle_next_inner_iter(self):
        self.__color_considered_rectangles(self.inner_index)
        self.__swap_if_greater(self.inner_index)
        self.__color_considered_rectangles(self.inner_index)
        self.inner_index += 1
        if self.inner_index >= len(self.recs):
            self.inner_index = 1

    def __draw_rectangle(self):
        pass
    
    def __draw_rectangles(self):
        pass

    def __next_outer_iteration(self):
        pass

    def __next_inner_iteration(self):
        pass

    def __previous_outer_state(self):
        pass
    
    def __previous_inner_state(self):
        pass

    def __draw_rectangles(self):
        pass

    def __draw__rectangle(self):
        pass
