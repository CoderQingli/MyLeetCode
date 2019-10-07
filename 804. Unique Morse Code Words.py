def uniqueMorseRepresentations(self, words):
    """
    :type words: List[str]
    :rtype: int
    """
    Morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
             ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    morsecode = []
    for word in words:
        morsecode.append("".join(Morse[ord(c) - ord("a")] for c in word))
    return len(set(morsecode))