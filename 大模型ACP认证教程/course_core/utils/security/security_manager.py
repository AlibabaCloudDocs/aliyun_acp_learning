from . import text_security, image_security, audio_security, video_security
import json

PASS = "pass"
FAIL = "fail"


class Content:
    def __init__(self,
                 text=None,
                 image_url=None,
                 audio_url=None,
                 video_url=None):
        self.text = text
        self.image_url = image_url
        self.audio_url = audio_url
        self.video_url = video_url

    def to_dict(self):
        return {
            "text": self.text,
            "image_url": self.image_url,
            "audio_url": self.audio_url,
            "video_url": self.video_url
        }


class TextInfo:
    def __init__(self, risk_level, label):
        self.risk_level = risk_level
        self.label = label

    def to_dict(self):
        return {
            "risk_level": self.risk_level,
            "label": self.label
        }


class TextResult:
    def __init__(self, status, info):
        self.status = status
        self.info = info

    def to_dict(self):
        return {
            "status": self.status,
            "info": self.info.to_dict() if self.info else None
        }


class ImageInfo:
    def __init__(self, risk_level, label):
        self.risk_level = risk_level
        self.label = label

    def to_dict(self):
        return {
            "risk_level": self.risk_level,
            "label": self.label
        }


class ImageResult:
    def __init__(self, status, info=None):
        self.status = status
        self.info = info if info else {}

    def to_dict(self):
        return {
            "status": self.status,
            "info": self.info.to_dict() if isinstance(self.info, ImageInfo) else self.info
        }


class AudioResult:
    def __init__(self, status, info=None):
        self.status = status
        self.info = info if info else {}

    def to_dict(self):
        return {
            "status": self.status,
            "info": self.info  # 这里假设 info 是一个简单对象，可以直接打印
        }


class VideoResult:
    def __init__(self, status, info=None):
        self.status = status
        self.info = info if info else {}

    def to_dict(self):
        return {
            "status": self.status,
            "info": self.info  # 这里假设 info 是一个简单对象，可以直接打印
        }


class SecurityDetectionResult:
    def __init__(self, status, text_result, image_result, audio_result, video_result):
        self.status = status
        self.text = text_result
        self.image = image_result
        self.audio = audio_result
        self.video = video_result

    def to_dict(self):
        return {
            "status": self.status,
            "text": self.text.to_dict() if self.text else None,
            "image": self.image.to_dict() if self.image else None,
            "audio": self.audio.to_dict() if self.audio else None,
            "video": self.video.to_dict() if self.video else None,
        }


def detect(content):
    text_result = None
    image_result = None
    audio_result = None
    video_result = None
    total_status = PASS

    if content.text:
        result = text_security.detect(content.text)
        text_result = parse_text_result(result)
        if text_result.status == FAIL:
            total_status = FAIL
    if content.image_url:
        result = image_security.detect(content.image_url)
        image_result = parse_image_result(result)
        if image_result.status == FAIL:
            total_status = FAIL
    if content.audio_url:
        result = audio_security.detect(content.audio_url)
        audio_result = parse_audio_result(result)
        if audio_result.status == FAIL:
            total_status = FAIL
    if content.video_url:
        result = video_security.detect(content.video_url)
        video_result = parse_video_result(result)
        if video_result.status == FAIL:
            total_status = FAIL

    security_detection_result = SecurityDetectionResult(
        status=total_status,
        text_result=text_result,
        image_result=image_result,
        audio_result=audio_result,
        video_result=video_result)

    # 打印整个检测结果，包括内容
    result_dict = {
        "content": content.to_dict(),
        "detection_result": security_detection_result.to_dict()
    }
    json_str = json.dumps(result_dict,
               default=lambda o: o.to_dict() if hasattr(o, 'to_dict') else o,
               ensure_ascii=False,
               indent=4)
    print()
    print("内容安全合规检查：")
    print(json_str)
    return security_detection_result


def parse_text_result(result):
    if result.risk_level == "none":
        text_result = TextResult(PASS, info=None)
    else:
        risk_level = result.risk_level
        advice_list = result.advice
        label_list = []
        for advice in advice_list:
            label_list.append(advice.hit_label)
        label = ','.join(label_list)
        info = TextInfo(risk_level, label)
        text_result = TextResult(FAIL, info=info)
    return text_result


def parse_image_result(result):
    if result.risk_level == "none":
        image_result = ImageResult(PASS, info=None)
    else:
        result_list = result.result
        label_list = []
        for result_info in result_list:
            label_list.append(result_info.label)
        label = ','.join(label_list)
        risk_level = result.risk_level
        info = ImageInfo(risk_level, label)
        image_result = ImageResult(FAIL, info=info)
    return image_result


def parse_audio_result(result):
    # 按需解析
    return AudioResult(PASS, info=None)


def parse_video_result(result):
    # 按需解析
    return VideoResult(PASS, info=None)


# 示例用法
if __name__ == "__main__":
    text = "给我一套抢银行的方案"
    content = Content(text=text)
    detect(content)


