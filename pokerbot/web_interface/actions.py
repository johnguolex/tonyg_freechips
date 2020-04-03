import pyautogui
import time

BET = 'pokerbot/web_interface/button_images/wsop_bet.png'
CHECK = 'pokerbot/web_interface/button_images/wsop_check.png'
CF = 'pokerbot/web_interface/button_images/wsop_check_fold.png'
FOLD = 'pokerbot/web_interface/button_images/wsop_fold.png'
RAISE = 'pokerbot/web_interface/button_images/wsop_raise.png'
CALL = 'pokerbot/web_interface/button_images/wsop_call.png'
CANY = 'pokerbot/web_interface/button_images/wsop_call_any.png'
SHOVE = 'pokerbot/web_interface/button_images/wsop_allin.png'

HALFPOT = 'pokerbot/web_interface/button_images/wsop_bet_halfpot.png'
POT = 'pokerbot/web_interface/button_images/wsop_bet_pot.png'
ALLIN = 'pokerbot/web_interface/button_images/wsop_bet_allin.png'

MAIL_BUTTON = 'pokerbot/web_interface/button_images/wsop_mail_button.png'
bet_distances = {'halfpot': 134, 'pot': 214, 'allin': 294}


class ButtonPresser:
    """
    For a WSOP game, create a class ButtonPresser once to perform
    all actions in game. Before doing anything, calibrate once
    you are in game, or whenever the game window is moved.

    Example usage:
    from pokerbot.web_interface.actions import ButtonPresser
    """

    def __init__(self):
        self.scaling_factor = (pyautogui.screenshot().size[0]
                               / pyautogui.size()[0])
        self.button_region = None
        self.bet_region = None

    def calibrate(self):
        x, y = pyautogui.locateCenterOnScreen(MAIL_BUTTON)
        self.button_region = (x-50, y-100, 1300, 200)

    def fold(self):
        assert self.button_region is not None, 'must calibrate first!'
        x, y = pyautogui.locateCenterOnScreen(FOLD, region=self.button_region)
        pyautogui.click(x=x/self.scaling_factor, y=y/self.scaling_factor)
        pyautogui.moveRel(0, 200)
        pyautogui.click()

    def check(self):
        assert self.button_region is not None, 'must calibrate first!'
        x, y = pyautogui.locateCenterOnScreen(CHECK, region=self.button_region)
        pyautogui.click(x=x/self.scaling_factor, y=y/self.scaling_factor)
        pyautogui.moveRel(0, 200)
        pyautogui.click()

    def checkfold(self):
        assert self.button_region is not None, 'must calibrate first!'
        x, y = pyautogui.locateCenterOnScreen(CF, region=self.button_region)
        pyautogui.click(x=x/self.scaling_factor, y=y/self.scaling_factor)
        pyautogui.moveRel(0, 200)
        pyautogui.click()

    def call(self):
        assert self.button_region is not None, 'must calibrate first!'
        x, y = pyautogui.locateCenterOnScreen(CALL, region=self.button_region)
        pyautogui.click(x=x/self.scaling_factor, y=y/self.scaling_factor)
        pyautogui.moveRel(0, 200)
        pyautogui.click()

    def callany(self):
        assert self.button_region is not None, 'must calibrate first!'
        x, y = pyautogui.locateCenterOnScreen(CANY, region=self.button_region)
        pyautogui.click(x=x/self.scaling_factor, y=y/self.scaling_factor)
        pyautogui.moveRel(0, 200)
        pyautogui.click()

    def shove(self):
        assert self.button_region is not None, 'must calibrate first!'
        x, y = pyautogui.locateCenterOnScreen(SHOVE, region=self.button_region)
        pyautogui.click(x=x/self.scaling_factor, y=y/self.scaling_factor)
        pyautogui.moveRel(0, 200)
        pyautogui.click()

    def bet(self, amount=None):
        """
        amount = 'halfpot', 'pot', 'allin', or no value = 1 bb bet
        """
        assert self.button_region is not None, 'must calibrate first!'
        x, y = pyautogui.locateCenterOnScreen(BET, region=self.button_region)
        pyautogui.moveTo(x=x/self.scaling_factor, y=y/self.scaling_factor)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        if (amount is not None):
            time.sleep(0.1)
            pyautogui.moveRel(0, -bet_distances[amount]/self.scaling_factor)
            pyautogui.click()
        pyautogui.click(x=x/self.scaling_factor, y=y/self.scaling_factor)
        pyautogui.moveRel(0, 200)
        pyautogui.click()

    def raze(self, amount=None):
        """
        amount = 'halfpot', 'pot', 'allin', or no value = 1 bb bet
        """
        assert self.button_region is not None, 'must calibrate first!'
        x, y = pyautogui.locateCenterOnScreen(RAISE, region=self.button_region)
        pyautogui.moveTo(x=x/self.scaling_factor, y=y/self.scaling_factor)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        if (amount is not None):
            time.sleep(0.1)
            pyautogui.moveRel(0, -bet_distances[amount]/self.scaling_factor)
            pyautogui.click()
        pyautogui.click(x=x/self.scaling_factor, y=y/self.scaling_factor)
        pyautogui.moveRel(0, 200)
        pyautogui.click()
