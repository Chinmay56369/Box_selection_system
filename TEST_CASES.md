# Test Cases

| ID | Test | Expected Result |
|---|---|---|
| TC-01 | Product fits in all boxes | Cheapest box selected |
| TC-02 | Product requires rotation | Rotation accepted |
| TC-03 | Product exceeds small box weight | Small box rejected |
| TC-04 | Product cannot fit any box | Error returned |
| TC-05 | Empty order | Error returned |
| TC-06 | Valid API request | HTTP 200 |
| TC-07 | Invalid order_id | HTTP 400 |
| TC-08 | Non-existent order | HTTP 404 |
| TC-09 | Invalid JSON | HTTP 400 |
| TC-10 | Order volume exceeds box | Box rejected |