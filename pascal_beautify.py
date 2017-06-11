import sublime
import sublime_plugin
import re


class PascalBeautifyCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        currentSyntax = self.view.settings().get('syntax').split('/')[-1].split('.')[0]
        if (currentSyntax != "Pascal"):
            print "Plugin works only with Pascal"
            return
        try:
            edit = self.view.begin_edit()
            for line in self.view.lines(sublime.Region(0, self.view.size())):
                currentLine = self.view.substr(line)
                # Add space after comma
                currentLine = re.sub(',(?![ \r\n])', ', ', currentLine)
                # Add space on either side of math symbols
                currentLine = re.sub('(?<![ \r\n\[\(\/])([+\-*\/%\^])(?![\/ \r\n])', r' \1 ', currentLine)
                # Add space on either side of assign symbol
                currentLine = re.sub('(?<![ \r\n])(:=)(?![ \r\n])', r' \1 ', currentLine)
                # Add space on either side of equal symbol
                currentLine = re.sub('(?<![ \r\n:<>])(=)(?![ \r\n])', r' \1 ', currentLine)
                # Add space on either side of compare symbol
                currentLine = re.sub('(?<![ \r\n<>])([<>])(?![<>= \r\n])', r' \1 ', currentLine)
                # Add space on either side of shift left symbol
                currentLine = re.sub('(?<![ \r\n])(<<)(?![ \r\n])', r' \1 ', currentLine)
                # Add space on either side of shift right symbol
                currentLine = re.sub('(?<![ \r\n])(>>)(?![ \r\n])', r' \1 ', currentLine)
                # Add space on either side of less or equal
                currentLine = re.sub('(?<![ \r\n])(<=)(?![ \r\n])', r' \1 ', currentLine)
                # Add space on either side of more or equal
                currentLine = re.sub('(?<![ \r\n])(>=)(?![ \r\n])', r' \1 ', currentLine)
                # Add space on left side of comments
                currentLine = re.sub('(?<![ \r\n])(\/\/)', r'  \1', currentLine)
                # Add space on right side of comments
                currentLine = re.sub('(\/\/)(?![ \r\n])', r'\1 ', currentLine)
                self.view.replace(edit, line, currentLine)
        finally:
            self.view.end_edit(edit)
