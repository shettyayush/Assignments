file="books.txt"

view_books() {
    echo "----------- BOOK LIST -----------"
    column -t -s, "$file"
}

search_book() {
    read -p "Enter Book Name: " name
    grep -i "$name" "$file"
}

count_out_of_stock() {
    awk -F, '$4=="OutOfStock"{count++}
    END{print "Out Of Stock Books:",count+0}' "$file"
}

update_status() {
    read -p "Enter Book ID: " id
    read -p "Enter New Status (Available/OutOfStock): " status

    awk -F, -v id="$id" -v st="$status" '
    BEGIN{OFS=","}
    {
        if($1==id)
            $4=st
        print
    }' "$file" > temp.txt

    mv temp.txt "$file"

    echo "Status Updated Successfully!"
}

inventory_value() {
    awk -F, '
    {sum+=$5}
    END{
        print "Total Inventory Value:",sum
    }' "$file"
}

books_by_category() {
    read -p "Enter Category: " category

    echo "Books in Category: $category"

    awk -F, -v cat="$category" '
    {
        if (tolower($3) == tolower(cat))
            print
    }' "$file"
}

costliest_book() {
    awk -F, '
    BEGIN{max=0}

    {
        if($5>max){
            max=$5
            record=$0
        }
    }

    END{
        print "Costliest Book:"
        print record
    }' "$file"
}

while true
do
    echo
    echo "========= BOOK INVENTORY ========="
    echo "1. View Books"
    echo "2. Search Book"
    echo "3. Count Out Of Stock Books"
    echo "4. Update Book Status"
    echo "5. Total Inventory Value"
    echo "6. Books By Category"
    echo "7. Costliest Book"
    echo "8. Exit"
    echo "=================================="

    read -p "Enter Choice: " choice

    case $choice in
        1) view_books ;;
        2) search_book ;;
        3) count_out_of_stock ;;
        4) update_status ;;
        5) inventory_value ;;
        6) books_by_category ;;
        7) costliest_book ;;
        8) echo "Exiting..."; break ;;
        *) echo "Invalid Choice!" ;;
    esac
done
