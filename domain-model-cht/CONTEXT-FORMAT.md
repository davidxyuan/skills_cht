# CONTEXT.md 格式

CONTEXT.md 是 bounded context 的 domain glossary。它記錄 domain expert 也認得的詞，以及這些詞之間的關係。

## 目的

- 讓工程師、agent、產品討論使用同一組語言。
- 避免同一個詞在不同地方有不同意思。
- 把 domain 觀念從實作細節中分離出來。

## 範本

~~~markdown
# Context: Ordering

## Purpose

Ordering context 負責接收 customer order、追蹤 order lifecycle，並發布供其他 context 使用的 domain events。

## Ubiquitous Language

### Order

Customer 提出的購買意圖。Order 可以包含多個 Order Lines，並會經過 Draft、Placed、Cancelled 等狀態。

Not the same as: Cart, Invoice

### Order Line

Order 中的一個商品項目，包含 product、quantity 與 price at time of ordering。

## Relationships

- Order owns Order Lines.
- Customer places Orders.
- Invoice is created after Order is placed.

## Open Questions

- 是否允許 partial cancellation？
~~~

## 撰寫規則

- 使用 domain 語言，不使用 class、table、endpoint 作為主要定義。
- 若某詞容易混淆，加入 Not the same as。
- 只記錄已確認的詞；未確認的放到 Open Questions。
- 決策當下就更新，不要等到最後整理。
