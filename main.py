from pyfwc import FWCAPI
from pathlib import Path
import time

def save_modern_awards_data():
    # change your subscription key here
    YOUR_SUBSCRIPTION_KEY = ""

    # create API instance
    fwc = FWCAPI(subscription_key=YOUR_SUBSCRIPTION_KEY)

    # get list of awards
    list_of_awards = fwc.get_awards(name='')
    award_dict = dict(zip(list_of_awards['code'].str.strip(), list_of_awards['name'].str.strip()))

    # save data from api
    for award_code, award_name in award_dict.items():
        print(f"----- Retreiving data for {award_code}-{award_name} -----")
        #create folder for each award
        Path(
            f"./data/{award_code}-{award_name}").mkdir(parents=True, exist_ok=True)

        # save award information
        fwc.get_award(award_code).to_excel(
            f'./data/{award_code}-{award_name}/award.xlsx', index=False)
        time.sleep(1)
        # save classification information
        fwc.get_classifications(award_code).to_excel(
            f'./data/{award_code}-{award_name}/classifications.xlsx', index=False)
        time.sleep(1)
        # save pay rates information
        fwc.get_payrates(award_code).to_excel(
            f'./data/{award_code}-{award_name}/payrates.xlsx', index=False)
        time.sleep(1)
        # save penalties information
        fwc.get_penalties(award_code).to_excel(
            f'./data/{award_code}-{award_name}/penalties.xlsx', index=False)
        time.sleep(1)
        # save expense allowances information
        fwc.get_expense_allowances(award_code).to_excel(
            f'./data/{award_code}-{award_name}/expense-allowances.xlsx', index=False)
        time.sleep(1)
        # save penalties information
        fwc.get_wage_allowances(award_code).to_excel(
            f'./data/{award_code}-{award_name}/wage-allowances.xlsx', index=False)
        time.sleep(10)            

if __name__ == "__main__":
    save_modern_awards_data()
    print("----- Finished! -----")