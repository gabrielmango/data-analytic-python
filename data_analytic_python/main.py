import pandas as pd

from data_analytic_python.repeated.information import Info
from data_analytic_python.repeated.repeated_person import RepeatedPerson


def get_data():
    """Function to get only data with flag 'EXCLUIR' from database."""
    data = pd.read_csv('data\database.csv')
    return data[data['fl_excluir'] == 'EXCLUIR']


def main() -> None:
    """Main function of the data analysis script."""
    data = [
        Info(
            name='atendimento',
            locate='public.tb_pessoa',
            path=r'scripts\atendimento.sql',
        ),
        Info(
            name='documento',
            locate='public.tb_documento',
            path=r'scripts\documento.sql',
        ),
        Info(
            name='geralpessoa',
            locate='public.tb_geral_pessoa',
            path=r'scripts\geralpessoa.sql',
        ),
        Info(
            name='localidade',
            locate='public.tb_localidade',
            path=r'scripts\localidade.sql',
        ),
        Info(
            name='contato_telefone',
            locate='public.tb_telefone',
            path=r'scripts\contato_telefone.sql',
        ),
        Info(
            name='contato_email',
            locate='public.tb_email',
            path=r'scripts\contato_email.sql',
        ),
    ]

    for element in data:
        print(element.name)
        if element.name == 'atendimento':
            RepeatedPerson(get_data(), element, element.locate, False)
        else:
            RepeatedPerson(get_data(), element, element.locate, True)


if __name__ == '__main__':
    main()