#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#


# @lc code=start
class Account:
    def __init__(self, name="", emails=[]) -> None:
        # initialize an account with name and emails
        self.name = name
        self.emails = set()
        self.emails.update(emails)

    def merge_emails(self, account):
        # update emails from the parameter account
        self.emails.update(account.emails)

    def is_same(self, account):
        # check if two accounts are the same:
        # same name and at least one email in common
        if self.name != account.name:
            return False
        return len(self.emails.intersection(account.emails)) > 0

    def to_string(self):
        email_list = list(self.emails)
        email_list.sort()
        return [self.name] + email_list


class AccountBook:
    def __init__(self) -> None:
        self.account_book = []

    def merge_account(self, account):
        merged = False
        new_account_book = []  # new account book after merging

        # find if the account can be merged with existing accounts
        for acc in self.account_book:
            if acc.is_same(account):
                # merge the account in the account book to the parameter account
                account.merge_emails(acc)
                merged = True
            else:
                # put other accounts in the new account book
                new_account_book.append(acc)

        # if merge has happened, put the merged account in the new account book
        if merged:
            new_account_book.append(account)
        # update the account book
        self.account_book = new_account_book
        return merged

    def add_account(self, account):
        self.account_book.append(account)

    def to_string(self):
        res = []
        for acc in self.account_book:
            res.append(acc.to_string())
        return res


class Solution:
    def accountsMerge(self, accounts):
        account_book = AccountBook()
        for acc in accounts:
            emails = acc[1:]
            account = Account(acc[0], emails)
            if not account_book.merge_account(account):
                # if merging is not possible,
                # the account is identical to all others in the account book,
                # so add the account to the account book
                account_book.add_account(account)

        return account_book.to_string()


# @lc code=end
