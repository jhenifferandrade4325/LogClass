// Função para buscar os produtos e exibi-los no front-end
async function fetchProdutos() {
    try {
        const response = await fetch("/api/get/produtos");
        if (!response.ok) {
            throw new Error(`Erro: ${response.status}`);
        }

        const produtos = await response.json();

        const tabelaBody = document.querySelector("#produtos-tabela tbody");
        tabelaBody.innerHTML = ""; // Limpa a tabela antes de renderizar

        // Itera sobre a lista de produtos e os adiciona à tabela
        produtos.forEach(produto => {
            const row = document.createElement("tr");

            row.innerHTML = `
                <td>${produto.codigo}</td>
                <td>${produto.descricao}</td>
                <td>${produto.modelo}</td>
                <td>${produto.fabricante}</td>
                <td>${produto.numero_lote}</td>
                <td>${produto.enderecamento}</td>
            `;

            tabelaBody.appendChild(row);
        });

    } catch (error) {
        console.error("Erro ao buscar produtos:", error);
    }
}

// Chama a função ao carregar a página
window.onload = fetchProdutos;