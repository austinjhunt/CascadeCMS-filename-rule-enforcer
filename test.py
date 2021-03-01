from cascade8_filename_enforcer.enforcer import CascadeCMSFileNameRuleEnforcer
import os,json
from requests.utils import quote  
cpass = quote(os.environ.get('CASCADE_CMS_PASS',''))
cuser = os.environ.get('CASCADE_CMS_USER','')
restapi= os.environ.get('CASCADE_CMS_REST_API_BASE','')
rule_enforcer = CascadeCMSFileNameRuleEnforcer(
    cpass=cpass,
    cuser=cuser,
    restapi=restapi
)
site_dicts = []
site_name="redesign.cofc.edu"
site_id="fca49d0aac1e00090ad4228845233487"
site_dictionary = {
    site_name : {
        'bad_assets': rule_enforcer.traverse(
            current_parent_folder=f'{site_name}/media',
            site_full_assets_list=[],
            skip_sites=["_Auto-Migrated Global_", "_skeleton.cofc.edu"]
        )
    } 
} 
site_dictionary[site_name]['publish_result'] = rule_enforcer.publish_site(site_id)
site_dicts.append(site_dictionary)
with open('test_site_read_redesign.json', 'w') as f:
    json.dump(site_dicts, f)
print(f"Completed scan of site {site_name}")