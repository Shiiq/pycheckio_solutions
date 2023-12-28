# This function should take a string as an input
# and return the count of vowels (a, e, i, o, u) in the string.
# The function should be case-insensitive.
import time
import functools


def execution_time(func):
    @functools.wraps(func)
    def wrapper(test_str):
        start = time.perf_counter()
        res = func(test_str)
        total = time.perf_counter() - start
        print(total)
        return res
    return wrapper


@execution_time
def count_vowels(text: str) -> int:
    text = text.lower()
    vowels = {
        "a": 1,
        "e": 1,
        "i": 1,
        "o": 1,
        "u": 1
    }
    counter = sum([vowels.get(sym, 0) for sym in text])
    # vowels = "aeiou"
    # counter = sum([text.count(i) for i in vowels])
    return counter


# These "asserts" are used for self-checking
assert count_vowels("hello") == 2
assert count_vowels("openai") == 4
assert count_vowels("typescript") == 2
assert count_vowels("a") == 1
assert count_vowels("b") == 0
assert count_vowels("aeiou") == 5
assert count_vowels("AEIOU") == 5
assert count_vowels("The quick brown fox") == 5
assert count_vowels("Jumps over the lazy dog") == 6
assert count_vowels("") == 0
print("The mission is done! Click 'Check Solution' to earn rewards!")

x = "October 1 is a 2014 Nigerian psychological thriller film written by Tunde Babalola, produced and directed by Kunle Afolayan, and starring Sadiq Daba, Kayode Olaiya, and Demola Adedoyin. The film is set in the last months of Colonial Nigeria in 1960. It recounts the fictional story of Danladi Waziri (Daba), a police officer from Northern Nigeria, investigating a series of killings of young women in the remote Western Nigeria village of Akote just before 1 October 1960 – the date Nigeria gained independence from British colonial rule. October 1 was shot with a budget of US$2 million (₦315 million in 2013) in Lagos, Ilara-Mokin, Akure, and villages neighbouring Akure, using period costumes and props, from August to September 2013. The film premiered on 28 September 2014 and opened to international audiences on 3 October. The film earned just over ₦100 million (US$610,000 in 2014) within six months of its release; Afolayan blamed film piracy for the film's low earnings. October 1 deals with several themes, including the sexual abuse of children by religious authority figures, religious and ethnic conflict, politics in Colonial Nigeria, and Nigeria's unification and independence. Critics reviewed the film positively, praising its cinematography, production design and costuming, writing, and acting. The film also won several awards, including Best Feature Film, Best Screenplay, and Best Actor at the 2014 Africa International Film Festival. Police inspector Danladi Waziri is summoned by the British colonial authorities to present his findings on a series of rapes and murders of young women in Akote, a remote village in Western Nigeria. Upon his arrival in Akote, he is received by Sergeant Afonja, who tells him that a man on horseback being admired by several villagers is Prince Aderopo, the first of their community to graduate from university. As he begins his investigation, Waziri notices a pattern in the killings and concludes that the rapes and murders are the work of a serial killer. In the evening, while Aderopo is meeting with his childhood friends Tawa and Agbekoya in the village bar, one of his guards deserts his post to spend time with his lover. At the bar, Baba Ifa, the town's chief priest, warns Waziri and Afonja that the killings will continue until the murderer is satisfied. The next day, the dead body of the guard's lover is discovered. Waziri orders the arrest of Baba Ifa, but Afonja refuses. Waziri suspends him and replaces him with his deputy, Corporal Omolodun. The body of an Igbo girl is discovered and Omolodun trails the killer along a bush path; the killer then kills Omolodun. Okafor, the girl's father, and his fellow tribesmen capture a travelling Hausa man, claiming that he is the serial killer. The accused man is taken into custody, but he maintains his innocence and tells Waziri that the actual perpetrator was whistling a tune. Waziri informs his superiors that he has found the murderer and will be closing the case. Okafor throws a machete at the man during his transfer, piercing his heart; as he is dying, the man continues to insist that he did not kill the girl. After leaving a celebration of the investigation's closure, Waziri hears whistling and is assaulted by the killer. Although he is too drunk to identify him, he slowly remembers the killer's face as he recovers at Afonja's home. The next morning, he goes to the market square to observe the body language of Aderopo. Waziri visits Tawa and discovers that Aderopo and Agbekoya both received the same scholarship from Reverend Dowling, the village priest. Waziri visits Agbekoya, who reveals that Dowling molested him and Aderopo. At an independence celebration, Aderopo invites Tawa to their childhood hideout, which has been renovated. Waziri and Afonja attempt to trail them, but are unsuccessful; Agbekoya, the only other person who knows the location of the hideout, leads them there. As they arrive, Aderopo is about to make Tawa his sixth victim, symbolizing the six years that he was abused by Dowling. Waziri and Afonja save Tawa. Waziri subsequently presents his account of the investigation to the British, who instruct him to withhold Aderopo's identity; he reluctantly agrees to do so for the sake of a peaceful independence."

count_vowels(x)
