def check_status(service_name: str, is_online: bool) -> str:
    if is_online:
        return f"{service_name}: 정상 운영 중"
    return f"{service_name}: 점검 중"

if __name__ == "__main__":
    print(check_status("결제 서버", True))
    print(check_status("알림 서버", False))