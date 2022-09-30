def caesar_cipher(s, k):
    v = "abcdefghijklmnopqrstuvwxyz"
    v_up = v.upper()
    return "".join(
        list(
            map(
                lambda x: v[(v.index(x) + k) % len(v)]
                if x in v
                else v_up[(v_up.index(x) + k) % len(v_up)]
                if x in v_up
                else x,
                s,
            )
        )
    )
    # Write your code here
