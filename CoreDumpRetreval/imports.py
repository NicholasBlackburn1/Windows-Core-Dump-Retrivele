"""
this is where put the imports for the module are at
"""

import logging
from datetime import datetime
import smtplib, ssl

import configparser
import pathlib
import platform
import sys
from io import StringIO

from colorama import Fore, Back, Style
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText