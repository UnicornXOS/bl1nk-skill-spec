
# Strategic Web Research

Get comprehensive, well-planned research results by combining strategic thinking with neural search. The skill breaks down complex queries, searches intelligently, and synthesizes findings.

## What This Skill Does

- **Plans** research strategy using Sequential Thinking
- **Searches** using Exa's neural search (understands concepts, not just keywords)
- **Structures** findings with clear organization
- **Synthesizes** information with proper attribution

## How to Use

### Basic Research

```
Research the latest developments in large language model agents
```

The skill will:
1. Use Sequential Thinking to break down the query into sub-questions
2. Plan the most effective search strategy
3. Execute targeted Exa searches
4. Organize and structure findings
5. Present comprehensive results with clear attribution

### Deep Research

```
Research machine learning interpretability techniques - I need academic papers, recent blog posts, and industry applications
```

The skill will:
1. Recognize multiple content types requested
2. Plan search strategy for each type
3. Use Exa's filters (academic, news, general web)
4. Organize findings by content type
5. Provide comprehensive coverage with proper categorization

### Comparative Research

```
Compare Rust vs Go for systems programming
```

The skill will:
1. Generate sub-questions using Sequential Thinking:
   - What are Rust's strengths?
   - What are Go's strengths?
   - What do developers say about each?
   - Performance benchmarks
2. Search Exa for each aspect
3. Synthesize balanced comparison with proper attribution

## Why Sequential Thinking + Exa?

### Sequential Thinking Benefits
- **Strategic Planning**: Breaks complex queries into manageable sub-questions
- **Systematic Approach**: Ensures comprehensive coverage of the topic
- **Reasoning**: Helps identify gaps and connections between concepts
- **Structure**: Organizes research in a logical, hierarchical way

### Exa Strengths
- **Neural Search**: Understands concepts, not just keywords
- **Academic Content**: Excellent for papers and technical content
- **Semantic Matching**: Finds conceptually similar content with different terminology
- **Quality Filtering**: Prioritizes authoritative sources

### Together = Better
By combining strategic thinking with neural search:
- **Comprehensive**: Planned approach covers all angles
- **Intelligent**: Conceptual understanding finds relevant content
- **Organized**: Clear structure from planning to results
- **Efficient**: Targeted searches instead of broad queries

## Example Workflows

### Technology Evaluation

```
Research Kubernetes alternatives for small teams
```

Sequential Thinking breaks this into:
- What are the main K8s alternatives?
- Which are optimized for small teams?
- What are the trade-offs?

Exa searches find:
- Technical comparisons and architecture docs
- Developer experiences and tutorials
- Case studies from small teams

Results: Organized comparison with clear recommendations

### Market Research

```
Research trends in AI-powered customer service
```

Sequential Thinking structures as:
- Current state of AI customer service
- Emerging trends and technologies
- Key players and solutions
- Future predictions

Exa provides:
- Research papers and analyst reports
- Case studies and implementation guides
- News and recent developments

Results: Comprehensive market overview with timeline

### Problem Solving

```
Research solutions for Python asyncio memory leaks
```

Sequential Thinking organizes:
- Common causes of asyncio memory leaks
- Debugging approaches
- Known solutions and workarounds
- Prevention best practices

Exa finds:
- Technical documentation
- GitHub issues and discussions
- Blog posts from experienced developers

Results: Actionable solutions prioritized by effectiveness

## Files Included

- `research_framework.py` - Utilities for organizing and structuring research
- `synthesis_framework.md` - Methodology for synthesizing findings
- `SKILL.md` - This documentation

## Advanced Features

### Strategic Query Decomposition

Sequential Thinking breaks queries into:
- **Sub-questions**: Multiple angles of investigation
- **Dependencies**: Which questions build on others
- **Priorities**: What to search first
- **Synthesis plan**: How to combine findings

### Intelligent Search Execution

Exa searches are optimized for:
- **Content type**: Academic, news, general web
- **Recency**: Latest information when needed
- **Authority**: Prioritize trusted sources
- **Depth**: Full-text analysis, not just titles

### Structured Organization

Results organized by:
- **Theme**: Group related findings
- **Source type**: Papers, docs, blogs, news
- **Relevance**: Most important first
- **Confidence**: Clear attribution and sourcing

## Tips for Best Results

1. **Be specific**: "React state management patterns" > "React"
2. **Mention content types**: Add "academic papers", "tutorials", "news" if you have preferences
3. **Use comparison queries**: "X vs Y" triggers comparative analysis
4. **Request depth**: Say "comprehensive" or "quick overview" to adjust breadth
5. **Specify recency**: Add "recent", "2024", "latest" for time-sensitive topics
6. **Ask for structure**: Request "organized by theme" or "chronological" for specific organization

## How Sequential Thinking Helps

Before searching, the skill uses Sequential Thinking to:
1. **Analyze your query**: What are you really asking?
2. **Generate sub-questions**: Break complex queries into aspects
3. **Plan search strategy**: What to search for and in what order
4. **Anticipate gaps**: What might we miss? Search for that too
5. **Synthesize intelligently**: How do findings relate to each other?

This planning phase (takes ~3-10 seconds) dramatically improves result quality and organization.

## Technical Details

### Search Execution

1. **Planning**: Sequential Thinking generates 2-5 sub-questions (~5 seconds)
2. **Targeted Search**: Exa queried for each sub-question
3. **Organization**: Results grouped by theme and relevance
4. **Synthesis**: Findings combined with clear structure and attribution

### Performance

- **Planning phase**: 3-10 seconds (Sequential Thinking)
- **Search phase**: 2-5 seconds per sub-question
- **Average total**: 15-35 seconds
- **Timeout limit**: 60 seconds (usually completes well under)
- **Results**: Organized by theme with 10-20 sources

### Workflow

```
User Query
    โ“
Sequential Thinking Analysis
    โ“
Generate Sub-Questions (2-5)
    โ“
Execute Exa Searches (parallel when possible)
    โ“
Organize by Theme
    โ“
Synthesize Findings
    โ“
Present Structured Results
```

## Comparison to Direct Search

| Feature | Direct Exa Search | This Skill |
|---------|-------------------|------------|
| Query formulation | Single query | Multiple strategic sub-queries |
| Organization | Search engine's ranking | Thematic structure |
| Coverage | Single search perspective | Multi-angle investigation |
| Depth | One search depth | Layered, systematic exploration |
| Synthesis | Raw results | Organized findings with structure |

## Privacy & Data

- No search history stored
- Queries sent to Exa directly
- Results processed in secure E2B sandbox
- No personal data required
- Sequential Thinking reasoning happens in-sandbox

## Success Rate

**Target: 95%+**

High reliability because:
- Pure API calls (no local dependencies)
- Well-tested MCPs (Sequential Thinking: 73K calls, Exa: 96K calls)
- Simple two-MCP architecture
- Execution time well within 60s limit
- Based on real usage pattern: 416 occurrences in 14 days

## Troubleshooting

**Not finding what you need?**
- Try rephrasing query
- Add specific content type (papers, news, tutorials)
- Specify recency (recent, latest, 2024)
- Request more specific structure ("organize by X")

**Too many results?**
- Ask for "quick summary" or "top 5 findings"
- Use more specific query terms
- Request filtering by criteria

**Planning taking too long?**
- Sequential Thinking may take 5-10 seconds for complex queries
- This is normal and improves result quality
- Try simplifying the query if consistently slow

## Support

This skill is maintained by Smithery. For issues:
- Check that Exa and Sequential Thinking MCPs are connected
- Verify MCPs are responding
- Review execution time if hitting timeouts (rare)