from bandwidth.voice.models.api_create_call_request import ApiCreateCallRequest
import main

voiceBody = ApiCreateCallRequest()
voiceBody.to = "{to}"
voiceBody.mfrom = "{from}"
voiceBody.answer_url = "{url}"
voiceBody.application_id = "{app_id}"
voice_client.create_call("{account_id}", body=voiceBody)