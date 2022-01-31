import sagemaker

def setup_sagemaker_session():
    # 1. Get Sagemaker session
    # 2. Get default bucket
    # 3. Get sagemaker execution role

    sagemaker_session = sagemaker.Session()
    bucket = sagemaker_session.default_bucket()
    role = sagemaker.get_execution_role()    

    return sagemaker_session, bucket, role
