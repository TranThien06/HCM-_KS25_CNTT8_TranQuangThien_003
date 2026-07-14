def search_registration(self):
    #     keyword = input("Nhập tên học viên cần tìm: ").strip().lower()

    #     if not keyword:
    #         print(" Lỗi: Từ khóa tìm kiếm không được để trống!")
    #         return

    #     results = [r for r in self.registrations if keyword in r.student_name.lower() and r.course_name.lower()]
    #     for r in self.registrations:
    #         if results:
    #             print(f"\n Kết quả tìm kiếm cho tên học viên '{keyword}':")
    #             print(f"{r.student_name:<20} | {r.course_name:<20}")
    #         else:
    #             print(" Không tìm thấy khóa học phù hợp.")