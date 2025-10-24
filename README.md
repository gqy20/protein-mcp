# protein-mcp

FastMCP-based protein data access tools for bioinformatics research

## Description

This project provides a FastMCP server implementation for accessing protein data from the RCSB Protein Data Bank (PDB). It enables researchers to query and retrieve protein structure information through standardized MCP protocols.

## Features

- **FastMCP Server Implementation**: High-performance MCP server for protein data access
- **RCSB PDB Integration**: Direct access to the RCSB Protein Data Bank
- **Protein Structure Queries**: Search and retrieve protein structure data
- **Bioinformatics Tools**: Specialized tools for protein analysis
- **TypeScript Implementation**: Modern, type-safe implementation

## Installation

```bash
npm install protein-mcp
```

## Quick Start

```typescript
import { ProteinMCPServer } from 'protein-mcp';

// Initialize the server
const server = new ProteinMCPServer();
await server.start();
```

## API Documentation

### Available Tools

- **Protein Search**: Search for proteins by name, ID, or properties
- **Structure Retrieval**: Get detailed protein structure information
- **Ligand Information**: Retrieve ligand and binding site data
- **Quality Metrics**: Access protein structure quality assessments

## Development

```bash
# Install dependencies
npm install

# Run tests
npm test

# Build the project
npm build

# Start development server
npm run dev
```

## Contributing

Contributions are welcome! Please read the [Contributing Guidelines](CONTRIBUTING.md) before submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Citation

If you use this software in your research, please cite:

```
@software{protein_mcp,
  title={protein-mcp: FastMCP-based protein data access tools},
  author={Your Name},
  year={2024},
  url={https://github.com/gqy20/protein-mcp}
}
```

## Related Projects

- [FastMCP](https://github.com/fastmcp/fastmcp) - The MCP framework this project is built on
- [RCSB PDB](https://www.rcsb.org/) - Protein Data Bank
- [BioPython](https://biopython.org/) - Computational biology tools

## Support

For issues and questions:
- Open an issue on [GitHub Issues](https://github.com/gqy20/protein-mcp/issues)
- Check the [Documentation](https://github.com/gqy20/protein-mcp/wiki)