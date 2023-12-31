from re import sub


def clean_cfp(cpf: str) -> str:
    cpf_clean = sub(r"\D+", "", cpf)
    return cpf_clean


def generate_digit(partial_informed_cpf: str):
    get_reverse_cpf = partial_informed_cpf[::-1]

    accumulator = 0
    for index, value in enumerate(get_reverse_cpf):
        accumulator += (index + 2) * int(value)

    get_result_acummulator = (accumulator * 10) % 11

    return str(get_result_acummulator) if get_result_acummulator <= 9 else "0"


def validate_cfp(informed_cpf):
    get_clean_cpf = clean_cfp(informed_cpf)
    get_partial_cpf = get_clean_cpf[0:9]

    if is_sequence(informed_cpf):
        return {
            "status": False,
            "message": "CPF inválido. Você informou uma sequência.",
        }

    get_first_verifying_digit = generate_digit(get_partial_cpf)
    get_second_verifying_digit = generate_digit(
        get_partial_cpf + get_first_verifying_digit
    )
    get_cpf_generated = (
        get_partial_cpf + get_first_verifying_digit + get_second_verifying_digit
    )

    return (
        {"status": True, "message": "VÁLIDO", "data": get_clean_cpf}
        if get_clean_cpf == get_cpf_generated
        else {"status": False, "message": "INVÁLIDO", "data": get_clean_cpf}
    )


def is_sequence(cpf):
    get_first_char_cpf = cpf[0]
    get_is_sequence = get_first_char_cpf * len(cpf)

    return True if get_is_sequence == cpf else False
