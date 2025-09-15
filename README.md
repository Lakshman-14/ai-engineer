# Enterprise Cloud Data Storage Architecture Guide

A comprehensive guide to trillion-scale data storage solutions for AI/ML and analytics, featuring real-world examples from industry leaders like Netflix, Meta, Amazon, Uber, and Airbnb.

## 🚀 Live Demo

Visit the live application: [Enterprise Cloud Storage Architecture](https://lakshman-14.github.io/ai-engineer/)

## 📋 Features

- **Service Overview**: Compare cloud storage services across AWS, GCP, and Azure
- **Use Case Explorer**: Analyze different data access patterns and architectural recommendations
- **Architecture Patterns**: Learn about Lambda, Kappa, Data Lakehouse, and Event Sourcing architectures
- **Real-World Examples**: Detailed case studies from major tech companies

## 🛠️ Technology Stack

- **Frontend**: React 18 with TypeScript
- **Styling**: Tailwind CSS
- **Icons**: Lucide React
- **Build Tool**: Vite
- **Deployment**: GitHub Pages with Actions

## 🏗️ Local Development

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## 📦 Deployment

This project is automatically deployed to GitHub Pages using GitHub Actions. Every push to the `main` branch triggers a new deployment.

### Manual Deployment Steps:

1. Fork this repository
2. Go to repository Settings → Pages
3. Set Source to "GitHub Actions"
4. Push changes to `main` branch
5. Your site will be available at: `https://[username].github.io/ai-engineer/`

## 🎯 Project Structure

```
src/
├── components/          # React components
│   ├── Header.tsx
│   ├── ServiceComparison.tsx
│   ├── UseCaseExplorer.tsx
│   ├── ArchitectureDiagram.tsx
│   └── RealWorldExamples.tsx
├── data/               # Data models and mock data
│   ├── storageServices.ts
│   ├── useCases.ts
│   ├── architecturePatterns.ts
│   └── realWorldExamples.ts
└── App.tsx            # Main application component
```

## 🌟 Key Highlights

- **Production-Ready**: Built with enterprise-grade practices and patterns
- **Responsive Design**: Optimized for all device sizes
- **Performance**: Optimized bundle size and loading performance
- **Accessibility**: WCAG compliant design patterns
- **SEO Friendly**: Proper meta tags and semantic HTML

## 📊 Data Sources

The application includes curated data about:
- 9+ major cloud storage services
- 6+ use case patterns with architectural recommendations
- 4+ enterprise architecture patterns
- 5+ real-world company case studies

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Cloud service documentation from AWS, GCP, and Azure
- Architecture patterns from industry best practices
- Real-world examples from public engineering blogs and case studies
