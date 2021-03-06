# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 15:39:13 2018
Version: python 3.6
@author: MrYanc
"""
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class GUI(object):
    """docstring for ClassName"""
    def __init__(self):
        # main window
        self.win = tk.Tk();
        self.win.title('Stocks Ratings Scraper');
        self.win.geometry();
        self.win.resizable(0, 0);
        self.__add__menu__();
        self.__add__mainframe__();
        pass;

    '''
    function: 
    input: 
    output: 
    exception: 
    '''
    def setup(self, briefing, marketbeats):
        # set up
        self.set_briefing(briefing);
        self.set_marketbeats(marketbeats);
        pass;

    '''
    function: 
    input: 
    output: 
    exception: 
    '''
    def execute(self):
        self.win.mainloop();
        return True;
        pass;

    '''
    function: 
    input: 
    output: 
    exception: 
    '''
    def dispose(self):
        pass;
        
    '''
    function: add menu
    input: 
    output: 
    exception: 
    '''
    def __add__menu__(self):
        # window menu
        menuBar = tk.Menu(self.win);
        self.win.config(menu=menuBar);
        # file menu
        fileMenu = tk.Menu(menuBar, tearoff=0);
        fileMenu.add_command(label='Exit');
        # help menu
        helpMenu = tk.Menu(menuBar, tearoff=0);
        helpMenu.add_command(label='About');
        # add menu to menu bar
        menuBar.add_cascade(label='File', menu=fileMenu);
        menuBar.add_cascade(label='File', menu=helpMenu);
        pass;

    '''
    function: add main frame
    input: 
    output: 
    exception: 
    '''
    def __add__mainframe__(self):
        # main frame
        mainFrame = ttk.LabelFrame(self.win, text='   Briefing & MarketBeats   ');
        mainFrame.grid(column=0, row=0, sticky='WE', padx=10, pady=10);

        self.__add__start__data__label__(mainFrame);
        self.__add__end__data__label__(mainFrame);
        self.__add__file__path__label__(mainFrame);
        self.__add__start__button__label__(mainFrame);
        
        pass;

    '''
    function: add enter start data label
    input: 
    output: 
    exception: 
    '''
    def __add__start__data__label__(self, mainFrame):
        # start date label
        startDateLabel = ttk.Label(mainFrame, text='Start Date');
        startDateLabel.grid(column=0, row=0, sticky='W', padx=10, pady=10);
        self.startDate = tk.StringVar();
        startDateEntered = ttk.Entry(mainFrame, width=12, textvariable=self.startDate);
        startDateEntered.grid(column=1, row=0, sticky='W');
        startDateEntered.delete(0, tk.END);
        startDateEntered.insert(0, 'year-mo-da');
        pass;

    '''
    function: add enter end data label
    input: 
    output: 
    exception: 
    '''
    def __add__end__data__label__(self, mainFrame):
        # end date label
        endDateLabel = ttk.Label(mainFrame, text='End Date:');
        endDateLabel.grid(column=0, row=1, sticky='W', padx=10, pady=10);
        self.endDate = tk.StringVar();
        endDateEntered = ttk.Entry(mainFrame, width=12, textvariable=self.endDate);
        endDateEntered.grid(column=1, row=1, sticky='W');
        endDateEntered.delete(0, tk.END);
        endDateEntered.insert(0, 'year-mo-da');
        pass

    '''
    function: add enter save file directory label
    input: 
    output: 
    exception: 
    '''
    def __add__file__path__label__(self, mainFrame):
        filepathLable = ttk.Label(mainFrame, text='File Path:');
        filepathLable.grid(column=0, row=2, sticky='W', padx=10, pady=10);
        self.filepathLableEntered = ttk.Entry(mainFrame, width=30);
        self.filepathLableEntered.grid(column=1, row=2, sticky='W');
        self.filepathLableEntered.delete(0, tk.END);
        self.__add__file__path__select__button__(mainFrame);
        pass;

    '''
    function: add select directory button
    input: 
    output: 
    exception: 
    '''
    def __add__file__path__select__button__(self, mainFrame):
        button = tk.Button(mainFrame, text="Select", command=self.__file__path__select__button__pressed__);
        button.grid(column=3, row=2, sticky='W', padx=10, pady=10);
        pass;

    '''
    function: select button pressed function
    input: 
    output: 
    exception: 
    '''
    def __file__path__select__button__pressed__(self):
        self.directory = filedialog.askdirectory();
        self.filepathLableEntered.insert(0, self.directory);
        pass;

    '''
    function: add start button
    input: 
    output: 
    exception: 
    '''
    def __add__start__button__label__(self, mainFrame):
        button = tk.Button(mainFrame, text="Start", command=self.__start__button__pressed__);
        button.grid(column=1, row=3, sticky='W', padx=10, pady=10);
        pass

    '''
    function: start button pressed function
    input: 
    output: 
    exception: 
    '''
    def __start__button__pressed__(self):
        if self.directory is None:
            pass;
        if self.startDate is not None:
            pass;
        if self.endDate is not None:
            pass;
        self.briefing.execute(self.startDate.get(), self.endDate.get(), self.directory, 'csv');
        self.marketbeats.execute(self.startDate.get(), self.endDate.get(), self.directory, 'csv');
        pass;

    '''
    function: 
    input: 
    output: 
    exception: 
    '''
    def set_briefing(self, briefing):
        self.briefing = briefing;
        pass;

    '''
    function: 
    input: 
    output: 
    exception: 
    '''
    def set_marketbeats(self, marketbeats):
        self.marketbeats = marketbeats;
        pass;

def main():
    gui = GUI();
    # gui.setup();
    gui.execute();
    gui.dispose();
    pass;

if __name__ == "__main__":
    main();
    pass;