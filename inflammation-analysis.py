#!/usr/bin/env python3
"""Software for managing and analysing patients' inflammation data in our imaginary hospital."""

import argparse

from inflammation import models, views

class Observation:
    def __init__(self, day, value):
        self.day=day
        self.value=value

    def __str__(self):
        return str(self.value)

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Patient(Person):
    """ A patient in inflammation study"""
    def __init__(self, name):
        super().__init__(name)
        self.observations=[]

    def add_observations(selfself, value, day=None):
        if day is None:
            try:
                day=self.observations[-1].day + 1
            except IndexError:
                day=0

        new_observation= Observation(day, value)

        self.observations.append(new_observation)
        return new_observation
    def __str__(self):
        return self.name


def main(args):
    """The MVC Controller of the patient inflammation data system.

    The Controller is responsible for:
    - selecting the necessary models and views for the current task
    - passing data between models and views
    """
    in_files = args.infiles
    if not isinstance(in_files, list):
        in_files = [args.infiles]

    for filename in in_files:
        inflammation_data = models.load_csv(filename)

        view_data = {
            'average': models.daily_mean(inflammation_data),
            'max': models.daily_max(inflammation_data),
            'min': models.daily_min(inflammation_data)
        }

        views.visualize(view_data)
        views.text_represent(view_data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='A basic patient inflammation data management system')
    parser.add_argument(
        'infiles',
        nargs='+',
        help='Input CSV(s) containing inflammation series for each patient')

    args = parser.parse_args()

    main(args)
