STOP_WORDS = [
    'a',
    'but',
    'during',
    'hows',
    "it's",
    'said',
    'this',
    "we're",
    "who've",
    'about',
    'by',
    'each',
    'however',
    "it's",
    'says',
    'those',
    "we've",
    'whove',
    'above',
    'can',
    'either',
    'i',
    'its',
    'see',
    'through',
    "we've",
    'will',
    'across',
    "can't",
    'for',
    "i'd",
    "let's",
    'she',
    'to',
    'weve',
    'with',
    'after',
    "can't",
    'from',
    "i'd",
    "let's",
    "she'd",
    'too',
    'were',
    'within',
    'all',
    'cant',
    'given',
    "i'll",
    'lets',
    "she'd",
    'towards',
    'what',
    'without',
    'along',
    'cannot',
    'had',
    "i'll",
    'may',
    'shed',
    'under',
    "what's",
    "won't",
    'also',
    'could',
    'has',
    "i'm",
    'me',
    "she'll",
    'until',
    "what's",
    "won't",
    'am',
    "couldn't",
    'have',
    "i'm",
    'more',
    "she'll",
    'us',
    'whats',
    'would',
    'an',
    "couldn't",
    'having',
    'im',
    'most',
    'shell',
    'use',
    'when',
    "wouldn't" 'and',
    'couldnt',
    'he',
    "i've",
    'much',
    'should',
    'used',
    "when's",
    "wouldn't" 'any',
    'did',
    "he'd",
    "i've",
    'must',
    'since',
    'uses',
    "when's",
    'you',
    'are',
    "didn't",
    "he'd",
    'ive',
    'my',
    'so',
    'using',
    'whens',
    "you'd",
    "aren't",
    "didn't",
    'hed',
    'if',
    'no',
    'some',
    'very',
    'where',
    "you'd",
    "aren't",
    'didnt',
    "he'll",
    'in',
    'not',
    'such',
    'want',
    'whether',
    'youd',
    'arent',
    'do',
    "he'll",
    'instead',
    'now',
    'than',
    'was',
    'which',
    "you'll",
    'as',
    'does',
    'her',
    'into',
    'of',
    'that',
    "wasn't",
    'while',
    "you'll",
    'at',
    "doesn't",
    'here',
    'is',
    'on',
    'the',
    "wasn't",
    'who',
    'youll',
    'be',
    "doesn't",
    'hers',
    "isn't",
    'one',
    'their',
    'wasnt',
    "who'll",
    "you're",
    'because',
    'doesnt',
    'him',
    "isn't",
    'only',
    'them',
    'we',
    "who'll",
    "you're",
    'been',
    'doing',
    'himself',
    'isnt',
    'or',
    'then',
    "we'd",
    'wholl',
    'youre',
    'before',
    'done',
    'his',
    'it',
    'other',
    'there',
    "we'd",
    "who's",
    "you've",
    'being',
    "don't",
    'how',
    "it'll",
    'our',
    'therefore',
    "we'll",
    "who's",
    "you've",
    'between',
    "don't",
    "how's",
    "it'll",
    'out',
    'these',
    "we'll",
    'whos',
    'youve',
    'both',
    'dont',
    "how's",
    'itll',
    'over',
    'they',
    "we're",
    "who've",
    'your',
]
STOP_WORDS = {
    'a',
    'but',
    'during',
    'hows',
    'its',
    'said',
    'this',
    'were',
    'whove',
    'about',
    'by',
    'each',
    'however',
    'its',
    'says',
    'those',
    'weve',
    'whove',
    'above',
    'can',
    'either',
    'i',
    'its',
    'see',
    'through',
    'weve',
    'will',
    'across',
    'cant',
    'for',
    'id',
    'lets',
    'she',
    'to',
    'weve',
    'with',
    'after',
    'cant',
    'from',
    'id',
    'lets',
    'shed',
    'too',
    'were',
    'within',
    'all',
    'cant',
    'given',
    'ill',
    'lets',
    'shed',
    'towards',
    'what',
    'without',
    'along',
    'cannot',
    'had',
    'ill',
    'may',
    'shed',
    'under',
    "what's",
    "won't",
    'also',
    'could',
    'has',
    'im',
    'me',
    'shell',
    'until',
    'whats',
    'wont',
    'am',
    'couldnt',
    'have',
    'im',
    'more',
    'shell',
    'us',
    'whats',
    'would',
    'an',
    'couldnt',
    'having',
    'im',
    'most',
    'shell',
    'use',
    'when',
    'wouldnt',
    'and',
    'couldnt',
    'he',
    'ive',
    'much',
    'should',
    'used',
    'whens',
    'wouldnt',
    'any',
    'did',
    'hed',
    'ive',
    'must',
    'since',
    'uses',
    'whens',
    'you',
    'are',
    'didnt',
    'hed',
    'ive',
    'my',
    'so',
    'using',
    'whens',
    'youd',
    'arent',
    'didnt',
    'hed',
    'if',
    'no',
    'some',
    'very',
    'where',
    'youd',
    'arent',
    'didnt',
    'hell',
    'in',
    'not',
    'such',
    'want',
    'whether',
    'youd',
    'arent',
    'do',
    'hell',
    'instead',
    'now',
    'than',
    'was',
    'which',
    'youll',
    'as',
    'does',
    'her',
    'into',
    'of',
    'that',
    'wasnt',
    'while',
    'youll',
    'at',
    'doesnt',
    'here',
    'is',
    'on',
    'the',
    "wasn't",
    'who',
    'youll',
    'be',
    'doesnt',
    'hers',
    'isnt',
    'one',
    'their',
    'wasnt',
    'wholl',
    'youre',
    'because',
    'doesnt',
    'him',
    'isnt',
    'only',
    'them',
    'we',
    'wholl',
    'youre',
    'been',
    'doing',
    'himself',
    'isnt',
    'or',
    'then',
    'wed',
    'wholl',
    'youre',
    'before',
    'done',
    'his',
    'it',
    'other',
    'there',
    'wed',
    'whos',
    'youve',
    'being',
    'dont',
    'how',
    'itll',
    'our',
    'therefore',
    'well',
    'whos',
    'youve',
    'between',
    'dont',
    'hows',
    'itll',
    'out',
    'these',
    'well',
    'whos',
    'youve',
    'both',
    'dont',
    'hows',
    'itll',
    'over',
    'they',
    'were',
    'whove',
    'your',
    '',
}