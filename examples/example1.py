import neuropacs

def main():
    api_key = "m0ig54amrl87awtwlizcuji2bxacjm"
    server_url = "http://ec2-3-142-212-32.us-east-2.compute.amazonaws.com:5000"
    # server_url = "http://localhost:5000"
    product_id = "PD/MSA/PSP-v1.0"
    result_format = "TXT"

    # PRINT CURRENT VERSION
    version = neuropacs.PACKAGE_VERSION

    # INITIALIZE NEUROPACS SDK
    npcs = neuropacs.init(api_key, server_url)

    # GENERATE AN AES KEY
    aes_key = npcs.generate_aes_key()
    print(aes_key)

    # CONNECT TO NEUROPACS
    connection_id = npcs.connect(api_key, aes_key)
    print(connection_id)

    # # CREATE A NEW JOB
    # order_id = npcs.new_job(connection_id, aes_key)
    # print(order_id)

    # # UPLOAD AN IMAGE
    # npcs.upload_dataset("./dicom_examples/06_001",order_id,connection_id, aes_key)

    # # START A JOB
    # job = npcs.run_job(product_id, order_id, connection_id, aes_key)
    # print(job)

    # CHECK STATUS
    status = npcs.check_status("TEST", connection_id , aes_key)
    print(status)

    # GET RESULTS
    results = npcs.get_results(result_format, "TEST", connection_id, aes_key)
    print(results)


main()