#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#


# @lc code=start
class Account:
    def __init__(self, name="", emails=[]) -> None:
        self.name = name
        self.emails = set()
        self.emails.update(emails)

    def merge_emails(self, account):
        self.emails.update(account.emails)

    def is_same(self, account):
        if self.name != account.name:
            return False
        return len(self.emails.intersection(account.emails)) > 0

    def to_string(self):
        email_list = list(self.emails)
        email_list.sort()
        return [self.name] + email_list


class Roaster:
    def __init__(self) -> None:
        self.roaster = []

    def merge_account(self, account):
        flag = False
        new_roaster = []
        for acc in self.roaster:
            if acc.is_same(account):
                account.merge_emails(acc)
                flag = True
            else:
                new_roaster.append(acc)
        if flag:
            new_roaster.append(account)
        self.roaster = new_roaster
        return flag

    def add_account(self, account):
        self.roaster.append(account)

    def to_string(self):
        res = []
        for acc in self.roaster:
            res.append(acc.to_string())
        return res


class Solution:
    def accountsMerge(self, accounts):
        roaster = Roaster()
        for acc in accounts:
            emails = acc[1:]
            account = Account(acc[0], emails)
            if not roaster.merge_account(account):
                roaster.add_account(account)

        return roaster.to_string()


# @lc code=end
