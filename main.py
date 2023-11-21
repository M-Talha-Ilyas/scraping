import requests
import json
import csv
import pandas as pd

def make_request(offset, slug, search_location):

    url = "https://www.realtor.com/api/v1/rdc_search_srp?client_id=rdc-search-for-sale-search&schema=vesta"

    payload = json.dumps({
    "query": "\n  query ConsumerSearchQuery(\n    $query: HomeSearchCriteria!\n    $limit: Int\n    $offset: Int\n    $search_promotion: SearchPromotionInput\n    $sort: [SearchAPISort]\n    $sort_type: SearchSortType\n    $client_data: JSON\n    $bucket: SearchAPIBucket\n  ) {\n    home_search: home_search(\n      query: $query\n      sort: $sort\n      limit: $limit\n      offset: $offset\n      sort_type: $sort_type\n      client_data: $client_data\n      bucket: $bucket\n      search_promotion: $search_promotion\n    ) {\n      count\n      total\n      search_promotion {\n        name\n        slots\n        promoted_properties {\n          id\n          from_other_page\n        }\n      }\n      properties: results {\n        property_id\n        list_price\n        search_promotions {\n          name\n          asset_id\n        }\n        primary_photo(https: true) {\n          href\n        }\n        rent_to_own {\n          right_to_purchase\n          rent\n        }\n        listing_id\n        matterport\n        virtual_tours {\n          href\n          type\n        }\n        status\n        products {\n          products\n          brand_name\n        }\n        source {\n          id\n          type\n          spec_id\n          plan_id\n          agents {\n            office_name\n          }\n        }\n        lead_attributes {\n          show_contact_an_agent\n          opcity_lead_attributes {\n            cashback_enabled\n            flip_the_market_enabled\n          }\n          lead_type\n          ready_connect_mortgage {\n            show_contact_a_lender\n            show_veterans_united\n          }\n        }\n        community {\n          description {\n            name\n          }\n          property_id\n          permalink\n          advertisers {\n            office {\n              hours\n              phones {\n                type\n                number\n                primary\n                trackable\n              }\n            }\n          }\n          promotions {\n            description\n            href\n            headline\n          }\n        }\n        permalink\n        price_reduced_amount\n        description {\n          name\n          beds\n          baths_consolidated\n          sqft\n          lot_sqft\n          baths_max\n          baths_min\n          beds_min\n          beds_max\n          sqft_min\n          sqft_max\n          type\n          sub_type\n          sold_price\n          sold_date\n        }\n        location {\n          street_view_url\n          address {\n            line\n            postal_code\n            state\n            state_code\n            city\n            coordinate {\n              lat\n              lon\n            }\n          }\n          county {\n            name\n            fips_code\n          }\n        }\n        open_houses {\n          start_date\n          end_date\n        }\n        branding {\n          type\n          name\n          photo\n        }\n        flags {\n          is_coming_soon\n          is_new_listing(days: 14)\n          is_price_reduced(days: 30)\n          is_foreclosure\n          is_new_construction\n          is_pending\n          is_contingent\n        }\n        list_date\n        photos(limit: 2, https: true) {\n          href\n        }\n        advertisers {\n          type\n          builder {\n            name\n            href\n            logo\n          }\n        }\n      }\n    }\n  }\n",
    "variables": {
        "geoSupportedSlug": slug,
        "query": {
        "primary": True,
        "status": [
            "for_sale",
            "ready_to_build"
        ],
        "search_location": {
            "location": search_location
        }
        },
        "client_data": {
        "device_data": {
            "device_type": "desktop"
        }
        },
        "limit": 200,
        "offset": offset,
        "sort_type": "relevant",
        "search_promotion": {
        "name": "POSTALCODE",
        "slots": [],
        "promoted_properties": [
            []
        ]
        }
    },
    "seoPayload": {
        "asPath": "/realestateandhomes-search/10016/pg-1",
        "pageType": {
        "silo": "search_result_page",
        "status": "for_sale"
        },
        "county_needed_for_uniq": False,
        "isFaqSupport": False
    },
    "isClient": True,
    "visitor_id": "0d3c6ec0-a671-419c-9983-11701679d967"
    })
    headers = {
    'authority': 'www.realtor.com',
    'accept': 'application/json, text/javascript',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'cookie': 'split=n; split_tcv=160; __vst=0d3c6ec0-a671-419c-9983-11701679d967; __ssn=0eb3a3e4-3c1d-4a36-a5db-b2e5355c4d10; __ssnstarttime=1700545480; __bot=false; permutive-id=675832b9-e452-4c93-a7f8-e968d557b69e; _pxvid=124cdc8b-8831-11ee-8b02-e6b5fad6740d; pxcts=124ce9de-8831-11ee-8b02-d5b6a8e05d7b; AWSALBTG=tPar21IzCR0l7octXzOILoU2MSJZzVDHvbg9m/6f4bMur2DH99lQOyDfYw1IubP1MfUQv97UCw2KOdF4aeyL2ol/u+VayLN1Wyz70E54HrnAT1cj+C03qcCzvk7ZreH4A+gOrUDuBYnYdaz7nNqnvmJ+h/IfCdoCdLMdacjdoQ2P; AWSALBTGCORS=tPar21IzCR0l7octXzOILoU2MSJZzVDHvbg9m/6f4bMur2DH99lQOyDfYw1IubP1MfUQv97UCw2KOdF4aeyL2ol/u+VayLN1Wyz70E54HrnAT1cj+C03qcCzvk7ZreH4A+gOrUDuBYnYdaz7nNqnvmJ+h/IfCdoCdLMdacjdoQ2P; AWSALB=vDJFH7nO94qOxhO2o6jQmrwXYG7dtlJ7YOjoEstENNOWAsYowLBzkbk82wGplHFnFa2PGx+jkLA1l+iyHmiFmDBYhHVG4c5jIMPP7f+OKy6qQoLMWj1fOtOKm4kQ; AWSALBCORS=vDJFH7nO94qOxhO2o6jQmrwXYG7dtlJ7YOjoEstENNOWAsYowLBzkbk82wGplHFnFa2PGx+jkLA1l+iyHmiFmDBYhHVG4c5jIMPP7f+OKy6qQoLMWj1fOtOKm4kQ; AMCVS_8853394255142B6A0A4C98A4%40AdobeOrg=1; __split=44; G_ENABLED_IDPS=google; _scid=5051ddca-f4e7-4788-9a0a-55989b5da3f2; _gcl_au=1.1.507110167.1700545486; _rdt_uuid=1700545485961.c6d7f147-651b-4039-b20c-30d7a49687b8; _tac=false~self|not-available; _ta=us~1~89df68bc35032d48c293adce8574aa42; _tas=91w765dv33r; _tt_enable_cookie=1; _ttp=Jnvm7TWzRE1I9-EJG2mtidtE3Fv; _ncg_sp_ses.cc72=*; _ncg_id_=4a535949-91fd-4ce2-a45d-cd5d24039e34; ajs_anonymous_id=9edab683-389f-4cc8-97c7-130b75717f54; s_ecid=MCMID%7C26885068079923027811358973231079988732; AMCV_8853394255142B6A0A4C98A4%40AdobeOrg=-1124106680%7CMCIDTS%7C19683%7CMCMID%7C26885068079923027811358973231079988732%7CMCAAMLH-1701150284%7C3%7CMCAAMB-1701150284%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1700552687s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.2.0; _ncg_domain_id_=4a535949-91fd-4ce2-a45d-cd5d24039e34.1.1700545486552.1763617486552; _gid=GA1.2.1488919710.1700545488; _lr_sampling_rate=0; AMCVS_AMCV_8853394255142B6A0A4C98A4%40AdobeOrg=1; AMCV_AMCV_8853394255142B6A0A4C98A4%40AdobeOrg=-1124106680%7CMCMID%7C26885068079923027811358973231079988732%7CMCIDTS%7C19683%7CMCOPTOUT-1700552687s%7CNONE%7CvVersion%7C5.2.0; _ncg_g_id_=90fe79ed-6d46-44d6-b8c9-90b8a4b20d68.3.1700545487.1763617486552; __qca=P0-1354899211-1700545486890; _lr_retry_request=true; _lr_env_src_ats=false; g_state={"i_p":1700552688634,"i_l":1}; _sctr=1%7C1700506800000; ab.storage.userId.7cc9d032-9d6d-44cf-a8f5-d276489af322=%7B%22g%22%3A%22visitor_0d3c6ec0-a671-419c-9983-11701679d967%22%2C%22c%22%3A1700545503414%2C%22l%22%3A1700545503418%7D; ab.storage.deviceId.7cc9d032-9d6d-44cf-a8f5-d276489af322=%7B%22g%22%3A%2249ffdd74-48c6-6acb-7c8e-ecfbfab3379d%22%2C%22c%22%3A1700545503420%2C%22l%22%3A1700545503420%7D; leadid_token-27789EFE-7A9A-DB70-BB9B-97D9B7057DBB-01836014-7527-FD48-9B7F-1A40A9705CFE=E208EC60-3377-BAFE-2F2F-D95C6AD52DD7; mdLogger=false; kampyle_userid=c265-1e0e-f6e5-4c29-38c3-4f3c-993c-e6e3; kampyleUserSession=1700545513287; kampyleUserSessionsCount=1; srchID=cc2cc13db448495db670c4dc89b73d70; _iidt=1XuLez+YP4eIV1vyDBO6HbLI1/UGEbxmyGq/Ae3rtsI5mBpIkIAfGT1a984YFrCZG2NX8HbalUGQ3g==; _vid_t=e/m2uPwqc1MZM/tsF5Rs2Ifeq35mxR6rQ+Gku0Sq/mxJE3I8QBjvHVLmDwOOu8+zsqekPtP7mIIyrA==; __fp=H7rIcYAfL4GS1Gbv91o6; criteria=sprefix%3D%252Fnewhomecommunities%26area_type%3Dpostal_code%26city%3DNew%2520York%26pg%3D1%26state_code%3DNY%26state_id%3DNY%26loc%3DNew%2520York%252C%2520NY%26locSlug%3D10016%26postal_code%3D10016%26county_fips%3D36061%26county_fips_multi%3D36061; __gsas=ID=a5f9b1cb0b47dfdc:T=1700545518:RT=1700545518:S=ALNI_Mafnnbz-mkHuWLus6kWsgKG3KQq0g; kampyleUserPercentile=38.754013240928266; _ncg_sp_id.cc72=4a535949-91fd-4ce2-a45d-cd5d24039e34.1700545487.1.1700545551.1700545487.ddfb142a-b442-41ea-a1eb-fab0e9d7b3db; ab.storage.sessionId.7cc9d032-9d6d-44cf-a8f5-d276489af322=%7B%22g%22%3A%22d8806af5-f514-77b1-9767-1f75649c8e0d%22%2C%22e%22%3A1700547352178%2C%22c%22%3A1700545503416%2C%22l%22%3A1700545552178%7D; _scid_r=5051ddca-f4e7-4788-9a0a-55989b5da3f2; _ga_MS5EHT6J6V=GS1.1.1700545486.1.1.1700545554.0.0.0; adcloud={%22_les_v%22:%22y%2Crealtor.com%2C1700547354%22}; _ga=GA1.2.1209132053.1700545485; _gat=1; _uetsid=14a76b60883111ee86b5db6c34a76959; _uetvid=14a90aa0883111eeb0287d94cd35ecb4; _px3=2cc2f947ae9bcdaa7a169dcf1d753c957fc6b9e5a71e18eb29be3e1a6da7239f:kz43DT5g3p2FmKbI6CLUeeEnY2dEFDmzOrwbXGb6wDOpAsziMimWEdRmTg1tq9f4ceLkQFdFQHmPffJzjmXeaA==:1000:Y2c+bKx6HPC11p3lR9F3tnOx62sP1OkCvI0msSDnMxcWGTnmOTmNTxBTQDJ/axKO9Gu0YDV5NfxvQaqLpAtjICT2vIuAbrX5GlzzfxPt2f5RzbHQhob4an+EiGuSUibgm/uDrCaJOqs98qzQS7mUqXJb0XG/2oGgf4eo5R0/zCjaHI5Z7fgxLYtFUMVtBlVvMSk8q4oJlVyhdlxwjkoK7i/r3xiJ1aY/MOBoRt/vYp4=; kampyleSessionPageCounter=3; __bot=false; __vst=0d3c6ec0-a671-419c-9983-11701679d967; split=n; split_tcv=160',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM3ODU4NCIsImFwIjoiOTAwMDM5MzQ1IiwiaWQiOiJlOTQ0MDhlYjRlYzg1N2I1IiwidHIiOiIwY2RlNWU4MTMxYjQxMTc1NDg1MWE1MjlmZGE3NTYwMCIsInRpIjoxNzAwNTQ1NTY2MTczLCJ0ayI6IjEwMjI2ODEifX0=',
    'origin': 'https://www.realtor.com',
    'rdc-ab-test-client': 'rdc-search-for-sale',
    'referer': 'https://www.realtor.com/realestateandhomes-search/10016',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-0cde5e8131b411754851a529fda75600-e94408eb4ec857b5-01',
    'tracestate': '1022681@nr=0-1-378584-900039345-e94408eb4ec857b5----1700545566173',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    try:
        data = json.loads(response.text)
        total = data['data']['home_search']['total']   
        return data['data']['home_search']['properties'], total
    except:
        return None 


def parse_data(properties_):
    records_extracted = 0
    output_file_path = 'data.csv'
    with open(output_file_path, 'a+', newline='', encoding="utf-8") as file_w:
        headers = ['Title', 'ActualPrice', 'Status', 'MinPrice', 'Description', 'Street', 'PostalCode', 'State', 'StateCode', 'City', 'Latitude', 'Longitude', 'Url']
        writer = csv.DictWriter(file_w, fieldnames=headers)

        for property_ in properties_:
            final_data = {}
            try:
                title = property_['permalink']
                final_data['Title'] = title
            except:
                final_data['Title'] = None
            
            try:
                actual_price = property_['list_price']
                final_data['ActualPrice'] = '$' + str(actual_price)
            except:
                final_data['ActualPrice'] = None
                
            try:
                status = property_['status']
                final_data['Status'] = status
            except:
                final_data['Status'] = None
                
            try:
                min_price = property_['price_reduced_amount']
                if min_price:
                    final_data['MinPrice'] = '$' + str(min_price)
                else:
                    final_data['MinPrice'] = '$' + min_price
            except:
                final_data['MinPrice'] = None
            
            try:
                desc = []
                for key, val in property_['description'].items():
                    try:
                        row = key + ": " + val
                        desc.append(row)
                    except:
                        pass
                desc = ', '.join(desc)
                final_data['Description'] = desc
            except:
                final_data['Description'] = None
                
            try:
                add = property_['location']['address']
                
                try:
                    street = add['line']
                    final_data['Street'] = street
                except:
                    final_data['Street'] = None

                try:
                    postal_code = add['postal_code']
                    final_data['PostalCode'] = postal_code
                except:
                    final_data['PostalCode'] = None

                try:
                    state = add['state']
                    final_data['State'] = state
                except:
                    final_data['State'] = None

                try:
                    state_code = add['state_code']
                    final_data['StateCode'] = state_code
                except:
                    final_data['StateCode'] = None

                try:
                    city = add['city']
                    final_data['City'] = city
                except:
                    final_data['City'] = None

                try:
                    lat = add['coordinate']['lat']
                    final_data['Latitude'] = lat
                except:
                    final_data['Latitude'] = None

                try:
                    lon = add['coordinate']['lon']
                    final_data['Longitude'] = lon
                except:
                    final_data['Longitude'] = None

            except:
                final_data['Street'] = None
                final_data['PostalCode'] = None
                final_data['State'] = None
                final_data['StateCode'] = None
                final_data['City'] = None
                final_data['Latitude'] = None
                final_data['Longitude'] = None
                
            try:
                url = property_['permalink']
                final_data['Url'] = 'https://www.realtor.com/realestateandhomes-detail/' +url
            except:
                final_data['Url'] = None

            writer.writerow(final_data)

            records_extracted +=1

            # print(final_data)
            # print(final_data.keys())
    return records_extracted


if __name__ == "__main__":

    loations = [['10016', '10016, New York, NY'],      ## list of location 
                ['90650', '90650, Norwalk, CA'],
                ['60629', '60629, Chicago, IL'],
                ['77433', '77433, Cypress, TX'],
                ['92154', '92154, San Diego, CA']
                
                ]

    output_file_path = 'data.csv'
    with open(output_file_path, 'a+', newline='', encoding="utf-8") as file_w:
        headers = ['Title', 'ActualPrice', 'Status', 'MinPrice', 'Description', 'Street', 'PostalCode', 'State', 'StateCode', 'City', 'Latitude', 'Longitude', 'Url']
        writer = csv.DictWriter(file_w, fieldnames=headers)
        writer.writeheader()
    
    for i in loations:
        offset, records, total = 0, 0, 0
        while records<= total:
            data, total = make_request(offset, i[0], i[1])
            records += parse_data(data)
            offset+=42
            print(records, total)

    ### removing duplicate ### 
    df = pd.read_csv(output_file_path, dtype = str)
    df = df.dropna(axis = 1)
    df = df.drop_duplicates(keep='first')
    df.to_csv(output_file_path, index=False)