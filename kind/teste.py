import google.cloud.dlp_v2 as dlp

def create_dlp_job():
    dlp_client = dlp.DlpServiceClient()

    parent = f"projects/{project_id}/locations/{location}"
    template_id = "your-inspection-template-id"

    inspect_job = {
        "inspect_template_name": f"{parent}/inspectTemplates/{template_id}",
        "storage_config": {
            "datastore_options": {
                "partition_id": {
                    "project_id": project_id,
                    "namespace_id": "your-confluence-namespace",
                },
                "kind": "your-confluence-entity-kind",
            }
        },
        "inspect_config": {
            "include_quote": True
        },
    }

    response = dlp_client.create_dlp_job(
        request={"parent": parent, "inspect_job": inspect_job}
    )
    print("Job created: {}".format(response.name))
