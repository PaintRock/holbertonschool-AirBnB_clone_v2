#!/usr/bin/python3
""" Test Console Module """

import unittest
import sys
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """ Test cases for the HBNBCommand class """

    def setUp(self):
        """ Set up test environment """
        self.console = HBNBCommand()

    def tearDown(self):
        """ Clean up test environment """
        pass

    def test_quit(self):
        """ Test quit command """
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")

    def test_EOF(self):
        """ Test EOF command """
        with self.assertRaises(SystemExit):
            self.console.onecmd("EOF")

    def test_emptyline(self):
        """ Test emptyline method """
        self.assertEqual(self.console.emptyline(), None)

    def test_create(self):
        """ Test create command """
        with StringIO() as output:
            sys.stdout = output
            self.console.onecmd("create BaseModel")
            sys.stdout = sys.__stdout__
            self.assertEqual(output.getvalue(), "\n")

    def test_show(self):
        """ Test show command """
        with StringIO() as output:
            sys.stdout = output
            self.console.onecmd("show BaseModel")
            sys.stdout = sys.__stdout__
            self.assertEqual(output.getvalue(), "** instance id missing **\n")

    # Add more test cases for other commands as needed

if __name__ == "__main__":
    unittest.main()
