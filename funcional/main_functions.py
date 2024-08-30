def error(e):
    """
    import os
    import sys
    from datetime import date

    This function is designed to log errors by writing relevant information to a text file.

    :param e: The `error` function you provided is designed to handle and log errors that occur in your
    code. It takes an error object `e` as a parameter, which represents the exception that was raised
    """
    exc_type, _, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    path_erro = r'Path'
    today = date.today()
    name = str(fname) + '_' + str(today) + '.txt'
    arquivo = open(os.path.join(path_erro, name), 'w')
    arquivo.write(str(fname) + "\n")
    arquivo.write(str(e) + "\n")
    arquivo.write(str(exc_type) + "\n")
    arquivo.write(str(exc_tb.tb_lineno) + "\n")
    arquivo.close()


def create_chrome_driver_with_manager(download_dir=None, headless=False):
    """
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    Cria um WebDriver do Chrome usando o Selenium Manager.

    :param download_dir: Diretório onde você deseja baixar os arquivos
    :param headless: Se True, o navegador será executado em modo headless, padrão é False
    :return: Objeto WebDriver
    """
    chrome_options = webdriver.ChromeOptions()

    # Configurações de download
    if download_dir:
        prefs = {
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": True
        }
        chrome_options.add_experimental_option("prefs", prefs)

    # Modo headless
    if headless:
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")

    # O Selenium Manager gerencia automaticamente o ChromeDriver
    return webdriver.Chrome(options=chrome_options)


def clicking(path, driver, element='elemento selecionado', refresh=False, by=By.XPATH, limit=3, wait=True):
    """
    * path: caminho do elemento que será encontrado na página. Pode ser um xpath, um ID, um name e etc;
    * element: nome do elemento que será encontrado na página. Esse parâmetro tem como finalidade unicamente para melhor depuração. Pode ser omitido;
    * refresh: default False - tem como objetivo atualizar a página para tentar clicar no elemento. Utilizado para clicar em arquivos em listas de query;
    * by: default XPATH - método utilizado para localizar o elemento, como XPATH, ID, NAME, CSS_SELECTOR e etc;
    * limit: default 3 - quantidade de vezes que a função irá tentar clicar no elemento. Por padrão, cada tentativa leva 20 segundos. Se o elemento não for encontrado, retornará None;
    """

    if limit == 0:
        return None

    elif refresh:
        driver.refresh()

    try:
        if wait:
            wait = WebDriverWait(driver, 60)
            wait.until(ec.visibility_of_element_located((by, path)))

        click_object = driver.find_element(by, path)
        actions = ActionChains(driver)
        actions.move_to_element(click_object).perform()

        found_element = driver.find_element(by, path)
        print(f">>>Sucesso {element}>>>")

    except selenium.common.exceptions.InvalidSelectorException:
        print(f"<<<Erro ao {element}, tentando novamente>>>")
        found_element = clicking(
            element=element, path=path, refresh=refresh, by=by, limit=limit - 1, driver=driver)

    return found_element


def download_checker(folder):
    """
    import glob
    import time

    This Python function checks if there are any ongoing downloads in a specified folder and waits until
    they are completed.

    :param folder: The function `downloadChecker` takes a folder path as a parameter. It checks for
    files with names containing "tmp" and "crdownload" in the specified folder to monitor the progress
    of downloads. It waits until there are no more files with those names in the folder, indicating that
    the download has
    """
    folder = (folder)
    print(folder)

    total = 1
    while (total != 0):
        filenames = glob.glob(folder + "/*tmp*")
        total = len(filenames)
        time.sleep(3)

    total = 1
    while (total != 0):
        filenames = glob.glob(folder + "/*crdownload*")
        total = len(filenames)
        time.sleep(1)

    print("  *Download concluído*")


def dir_cleaner(path, delete_folder=True):
    """
    import os

    Função que limpa todos os arquivos do diretorio selecionado 
    - path: caminho do diretorio que sera limpado por completo
    """
    if (os.path.exists(Path(path))):

        for file in os.listdir(path):

            if os.path.isfile(path + '\\' + file):
                os.remove(path + '\\' + file)

            elif os.path.isdir(path + '\\' + file):
                dir_cleaner(path=path + '\\' + file)

                if delete_folder:
                    os.rmdir(path + "\\" + file)


def dir_editor(path, clean=False, delete=False):
    """
    import os

    The function creates a directory at the specified path and optionally cleans it if it already
    exists.

    :param path: The `path` parameter in the `dir_editor` function is the directory path where you want
    to create a new directory
    :param clean: The `clean` parameter in the `dir_editor` function is a boolean flag that determines 
    whether to clean the directory before creating it. If `clean` is set to `True`, the function will
    first clean the directory at the specified `path` before creating a new directory. If `clean,
    defaults to False (optional)
    """
    if os.path.isdir(path):
        if clean:
            cleanDir(path, False)
        if delete:
            dir_cleaner(path)
    else:
        os.mkdir(path)


def call_api(url):
    """
    import pandas as pd
    import requests

    This Python function makes repeated API calls with increasing page numbers until no more data is
    returned, concatenating the results into a single pandas DataFrame.

    :param url: The `url` parameter is a string representing the API endpoint that you want to call to
    retrieve data. The function `call_api` makes requests to this URL with pagination parameters to
    fetch data in batches of 10,000 records per page. It then processes the JSON response and appends
    the data
    :return: The function `call_api` is returning a pandas DataFrame that is a concatenation of all the
    DataFrames stored in the `df_list` variable. If `df_list` is empty, then an empty pandas DataFrame
    is returned.
    """
    i = 1
    df_list = []

    while True:
        try:
            response = requests.get(f"{url}?pageSize=10000&pageNum={i}")
            response.raise_for_status()  # Levanta exceções para status de erro HTTP
            result = response.json()

        except requests.exceptions.RequestException as e:
            print(f"Erro ao chamar a API: {e}")
            return None

        df = pd.DataFrame(result.get('list', []))

        if df.empty:
            if i == 1:
                return None
            else:
                break
        else:
            df_list.append(df)
            i += 1

    return pd.concat(df_list) if df_list else pd.DataFrame()
