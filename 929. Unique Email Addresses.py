def numUniqueEmails(self, emails):
    """
    :type emails: List[str]
    :rtype: int
    """
    e = set()
    for email in emails:
        local, domain = email.split("@")
        local = local.split("+")[0].replace(".", "")
        em = local + "@" + domain
        e.add(em)
    return len(e)